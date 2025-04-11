from flask import Flask, request, jsonify
from flask_cors import CORS
import spacy
import pdfplumber
import docx2txt
import re
from collections import Counter
from nltk.corpus import wordnet
from sentence_transformers import SentenceTransformer, util
from smart_keywords import SMART_KEYWORDS

app = Flask(__name__)
CORS(app)

# NLP models
nlp = spacy.load("en_core_web_sm")
model = SentenceTransformer('all-MiniLM-L6-v2')  # FREE semantic BERT model

# Generic words to ignore
GENERIC_STOPWORDS = set([
    "good", "high", "strong", "experience", "include", "ensure", "support", "help",
    "provide", "member", "team", "task", "manual", "process", "system", "develop",
    "engineer", "test", "testing", "workflow", "maintain", "problem", "solution", "work",
    "issue", "skill", "require", "effective", "understand", "tool", "technology", "create",
    "clear", "need", "field", "degree", "ability", "related", "review", "focus", "plus"
])

# ---------------------
# UTIL FUNCTIONS
# ---------------------
def parse_resume(file):
    if file.filename.endswith('.pdf'):
        with pdfplumber.open(file) as pdf:
            return ' '.join([page.extract_text() or '' for page in pdf.pages])
    elif file.filename.endswith('.docx'):
        return docx2txt.process(file)
    return ""

def extract_relevant_sections(text):
    text = text.strip()
    relevant_sections = []
    patterns = [
        r"(?i)Responsibilities\s*(.*?)(?=Required Qualifications|Preferred Experience|$)",
        r"(?i)Required Qualifications\s*(.*?)(?=Preferred Experience|$)",
        r"(?i)Preferred Experience\s*(.*?)(?=$)"
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            section = match.group(1).strip()
            if section:
                relevant_sections.append(section)
    return "\n".join(relevant_sections)

def extract_ats_keywords(text):
    doc = nlp(text)
    keywords = [
        token.lemma_.lower()
        for token in doc
        if token.pos_ in ["NOUN", "VERB", "PROPN", "ADJ"]
        and not token.is_stop
        and token.is_alpha
        and token.lemma_.lower() not in GENERIC_STOPWORDS
    ]
    ranked = Counter(keywords)
    return [kw for kw, freq in ranked.most_common(30)]

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().lower())
    return synonyms

def semantic_score(word, resume_keywords):
    word_emb = model.encode(word, convert_to_tensor=True)
    resume_embs = model.encode(resume_keywords, convert_to_tensor=True)
    similarities = util.pytorch_cos_sim(word_emb, resume_embs)
    max_score = float(similarities.max())
    return max_score

# ---------------------
# MATCHING LOGIC
# ---------------------
def match_concepts_detailed(resume_text):
    resume_lower = resume_text.lower()
    matched = []
    missing = []

    for key, value in SMART_KEYWORDS.items():
        found_phrases = [term for term in value["aliases"] if term in resume_lower]
        if found_phrases:
            matched.append({
                "concept": value["label"],
                "evidence": found_phrases[0],
                "description": value["description"]
            })
        else:
            missing.append({
                "concept": value["label"],
                "note": f"Could not find examples of {key} (e.g., {value['aliases'][0]})"
            })
    return matched, missing

# ---------------------
# MAIN ENDPOINT
# ---------------------
@app.route('/analyze', methods=['POST'])
def analyze():
    jd = request.form['job_description']
    resume = request.files['resume']
    resume_text = parse_resume(resume)

    relevant_jd_text = extract_relevant_sections(jd)

    jd_keywords = extract_ats_keywords(relevant_jd_text)
    resume_keywords = extract_ats_keywords(resume_text)

    # 1. Exact word matches
    matched_words = set(jd_keywords).intersection(set(resume_keywords))
    missing_words = set(jd_keywords) - matched_words
    word_score = round((len(matched_words) / len(jd_keywords)) * 100, 2) if jd_keywords else 0.0

    # 2. Synonym matching
    soft_matches = []
    soft_misses = []

    for word in missing_words:
        synonyms = get_synonyms(word)
        if synonyms.intersection(set(resume_keywords)):
            soft_matches.append(word)
        else:
            soft_misses.append(word)

    # 3. Semantic similarity
    semantic_hits = []
    for word in soft_misses:
        sim = semantic_score(word, resume_keywords)
        if sim > 0.6:
            semantic_hits.append(word)

    # Final list of missing = truly unmatched
    real_missing = set(soft_misses) - set(semantic_hits)

    # 4. Conceptual match
    matched_concepts, missing_concepts = match_concepts_detailed(resume_text)
    concept_score = round((len(matched_concepts) / len(SMART_KEYWORDS)) * 100, 2)

    # Final scores
    soft_score = round((len(soft_matches) + len(semantic_hits)) / len(jd_keywords) * 100, 2) if jd_keywords else 0.0
    overall_score = round((word_score + soft_score + concept_score) / 3, 2)

    return jsonify({
        "overall_match_percent": overall_score,
        "word_match_score": word_score,
        "synonym_semantic_match_score": soft_score,
        "concept_score": concept_score,
        "matched_keywords": sorted(list(matched_words)),
        "soft_matched_keywords": sorted(soft_matches + semantic_hits),
        "missing_keywords": sorted(list(real_missing)),
        "matched_concepts_detailed": matched_concepts,
        "missing_concepts_detailed": missing_concepts
    })

if __name__ == '__main__':
    app.run(debug=True)
