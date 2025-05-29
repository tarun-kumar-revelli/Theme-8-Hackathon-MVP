def get_owasp_vulnerability_context(vulnerability_name):
    # Stubbed function to return a fixed context string for a given OWASP vulnerability
    vulnerabilities = {
        "Injection": "Injection flaws, such as SQL, NoSQL, Command Injection, and others, occur when an attacker is able to send untrusted data to an interpreter as part of a command or query.",
        "Broken Authentication": "Application functions related to authentication and session management are implemented incorrectly, allowing attackers to compromise passwords, keys, or session tokens.",
        "Sensitive Data Exposure": "Sensitive data is not properly protected, allowing attackers to access it. This includes data at rest and in transit.",
        "XML External Entities (XXE)": "Older or poorly configured XML processors evaluate external entity references within XML documents, leading to potential data exposure.",
        "Broken Access Control": "Restrictions on what authenticated users are allowed to do are not properly enforced.",
        "Security Misconfiguration": "The application is insecure by default, and security settings are not defined, implemented, or maintained.",
        "Cross-Site Scripting (XSS)": "XSS flaws occur whenever an application includes untrusted data on a web page without proper validation or escaping.",
        "Insecure Deserialization": "Insecure deserialization flaws occur when untrusted data is used to abuse the logic of an application.",
        "Using Components with Known Vulnerabilities": "Libraries, frameworks, and other software modules run with the same privileges as the application. If a vulnerable component is exploited, it can facilitate serious data loss or server takeover.",
        "Insufficient Logging & Monitoring": "Insufficient logging and monitoring can allow attackers to maintain persistence, pivot to more systems, and cover their tracks."
    }
    return vulnerabilities.get(vulnerability_name, "Vulnerability context not found.")