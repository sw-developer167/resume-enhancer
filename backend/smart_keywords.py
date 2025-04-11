# smart_keywords_explained.py

SMART_KEYWORDS = {
    # Developer Productivity & DevOps
    "ci/cd pipelines": {
        "aliases": ["ci/cd", "jenkins", "github actions", "travis ci", "circleci", "build pipeline"],
        "label": "CI/CD Pipelines",
        "description": "Build and automate deployment pipelines using CI/CD tools like Jenkins, GitHub Actions, or CircleCI."
    },
    "developer dashboards": {
        "aliases": ["grafana", "custom dashboard", "metrics ui", "monitoring ui"],
        "label": "Developer Dashboards",
        "description": "Create dashboards for code quality, testing status, or system performance."
    },
    "collaboration": {
        "aliases": ["worked with engineers", "collaborate with devops", "cross-functional", "paired programming"],
        "label": "DevOps & Team Collaboration",
        "description": "Worked in cross-functional teams and collaborated with engineers and DevOps."
    },
    "on-call": {
        "aliases": ["on-call", "24/7 support", "incident response", "support rotation"],
        "label": "On-Call Support",
        "description": "Participated in on-call rotations and incident response for production systems."
    },
    "containerization": {
        "aliases": ["docker", "kubernetes", "helm"],
        "label": "Containerization",
        "description": "Used Docker and Kubernetes for containerizing applications and managing deployments."
    },
    "infrastructure as code": {
        "aliases": ["terraform", "cloudformation", "pulumi"],
        "label": "Infrastructure as Code",
        "description": "Managed infrastructure using code with tools like Terraform and CloudFormation."
    },
    "version control": {
        "aliases": ["git", "github", "bitbucket", "gitlab"],
        "label": "Version Control",
        "description": "Utilized version control systems like Git for source code management."
    },
    "test automation": {
        "aliases": ["junit", "espresso", "selenium", "automated testing", "pytest", "cypress", "jest", "mocha", "unit testing", "integration testing"],
        "label": "Test Automation",
        "description": "Implemented automated testing frameworks to ensure code quality and reliability."
    },
    "programming languages": {
        "aliases": ["python", "java", "go", "ruby", "kotlin", "typescript", "javascript", "c#", "c++", "php", "swift", "dart", "rust"],
        "label": "Programming Languages",
        "description": "Proficient in various programming languages used for software development."
    },
    "devops tools": {
        "aliases": ["aws", "azure", "gcp", "terraform", "jenkins", "docker", "kubernetes", "ansible", "cloudformation"],
        "label": "DevOps Tools",
        "description": "Experienced with DevOps tools for continuous integration, deployment, and infrastructure management."
    },
    "debugging/problem solving": {
        "aliases": ["debugging", "resolved issues", "problem solving", "bug fixes", "troubleshooting"],
        "label": "Debugging & Problem Solving",
        "description": "Skilled in identifying and resolving software issues and bugs."
    },
    "monitoring": {
        "aliases": ["monitoring", "logging", "prometheus", "datadog", "new relic", "splunk", "cloudwatch"],
        "label": "Monitoring & Logging",
        "description": "Implemented monitoring and logging solutions to track application performance."
    },

    # Android Development
    "android frameworks": {
        "aliases": ["android sdk", "jetpack", "mvvm", "room database", "viewmodel", "livedata", "navigation component"],
        "label": "Android Frameworks",
        "description": "Developed Android applications using frameworks like Jetpack and MVVM architecture."
    },
    "android networking": {
        "aliases": ["retrofit", "okhttp", "volley"],
        "label": "Android Networking",
        "description": "Handled network operations in Android apps using libraries like Retrofit and OkHttp."
    },
    "android testing": {
        "aliases": ["espresso", "robolectric", "uiautomator"],
        "label": "Android Testing",
        "description": "Performed automated testing of Android applications using Espresso and Robolectric."
    },
    "android architecture": {
        "aliases": ["mvvm", "mvp", "clean architecture"],
        "label": "Android Architecture",
        "description": "Applied architectural patterns like MVVM and Clean Architecture in Android development."
    },

    # Front-End Development
    "frontend frameworks": {
        "aliases": ["react", "angular", "vue", "svelte", "next.js"],
        "label": "Front-End Frameworks",
        "description": "Built user interfaces using front-end frameworks like React and Angular."
    },
    "frontend tools": {
        "aliases": ["webpack", "babel", "vite"],
        "label": "Front-End Tools",
        "description": "Utilized tools like Webpack and Babel for front-end development workflows."
    },
    "ui/ux": {
        "aliases": ["figma", "adobe xd", "user experience", "responsive design", "accessibility", "material ui", "bootstrap", "tailwindcss"],
        "label": "UI/UX Design",
        "description": "Designed user interfaces focusing on user experience and accessibility."
    },
    "web performance": {
        "aliases": ["lazy loading", "code splitting", "lighthouse", "core web vitals"],
        "label": "Web Performance Optimization",
        "description": "Optimized web applications for performance using techniques like lazy loading and code splitting."
    },

    # Back-End Development
    "backend frameworks": {
        "aliases": ["node.js", "express.js", "django", "spring boot", "flask", "fastapi", "ruby on rails", "laravel", ".net core"],
        "label": "Back-End Frameworks",
        "description": "Developed server-side applications using frameworks like Node.js and Django."
    },
    "api development": {
        "aliases": ["rest api", "graphql", "api gateway", "swagger", "postman"],
        "label": "API Development",
        "description": "Designed and implemented APIs using REST or GraphQL standards."
    },
    "authentication": {
        "aliases": ["oauth", "jwt", "auth0", "firebase auth"],
        "label": "Authentication & Authorization",
        "description": "Implemented authentication mechanisms using OAuth, JWT, and similar technologies."
    },
    "databases": {
        "aliases": ["mysql", "postgresql", "mongodb", "firebase", "redis", "oracle", "sql server", "cassandra", "dynamodb"],
        "label": "Databases",
        "description": "Managed and interacted with various databases for data storage and retrieval."
    },
    "message brokers": {
        "aliases": [
            "kafka", "rabbitmq", "activemq", "nats", "pulsar", "zeromq", "rocketmq", "mqtt",
            "amazon sqs", "azure service bus", "ibm mq", "google pub/sub", "solace", "memphis"
        ],
        "label": "Message Brokers",
        "description": "Experience with message brokers and event streaming platforms such as Apache Kafka, RabbitMQ, ActiveMQ, and others for building scalable, event-driven architectures."
    },
        # Full Stack Development
    "full stack": {
        "aliases": ["frontend", "backend", "restful services", "end-to-end development", "monolithic", "microservices", "api integration"],
        "label": "Full Stack Development",
        "description": "Proficient in both front-end and back-end development, enabling end-to-end application design and implementation."
    },

    # Web Development Fundamentals
    "web fundamentals": {
        "aliases": ["html", "css", "javascript", "dom manipulation"],
        "label": "Web Fundamentals",
        "description": "Skilled in core web technologies including HTML, CSS, JavaScript, and DOM manipulation."
    },
    "cross-browser": {
        "aliases": ["browser compatibility", "cross-browser testing"],
        "label": "Cross-Browser Compatibility",
        "description": "Ensured consistent functionality and appearance across multiple web browsers through thorough testing and optimization."
    },
    "state management": {
        "aliases": ["redux", "context api", "zustand", "mobx"],
        "label": "State Management",
        "description": "Managed application state effectively using tools like Redux, Context API, and other state management libraries."
    },
    "seo": {
        "aliases": ["seo optimization", "meta tags", "structured data"],
        "label": "Search Engine Optimization (SEO)",
        "description": "Optimized web applications for search engines by implementing best practices such as meta tags and structured data."
    },

    # Tools & Platforms
    "project management": {
        "aliases": ["jira", "trello", "confluence"],
        "label": "Project Management Tools",
        "description": "Utilized tools like Jira, Trello, and Confluence for efficient project tracking and collaboration."
    },
    "source control": {
        "aliases": ["git", "svn", "mercurial"],
        "label": "Source Control Systems",
        "description": "Experienced in version control systems such as Git, SVN, and Mercurial for code management and collaboration."
    },
    "cloud platforms": {
        "aliases": ["aws", "gcp", "azure", "firebase"],
        "label": "Cloud Platforms",
        "description": "Deployed and managed applications on cloud platforms including AWS, GCP, Azure, and Firebase."
    },
    "testing tools": {
        "aliases": ["jest", "mocha", "chai", "cypress", "testng"],
        "label": "Testing Tools",
        "description": "Implemented testing strategies using tools like Jest, Mocha, Chai, Cypress, and TestNG to ensure software quality."
    },

    # Development Methodologies
    "methodologies": {
        "aliases": ["agile", "scrum", "kanban", "sdlc", "tdd", "bdd", "pair programming"],
        "label": "Development Methodologies",
        "description": "Applied various development methodologies such as Agile, Scrum, Kanban, SDLC, TDD, BDD, and practiced pair programming for efficient software development."
    }
}
 
