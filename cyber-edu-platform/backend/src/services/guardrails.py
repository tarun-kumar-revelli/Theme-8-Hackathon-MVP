import guardrails as gd
from guardrails import Guard
from guardrails.validators import ValidLength, ToxicLanguage, RestrictToTopic
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class SecurityGuard:
    def __init__(self):
        # Initialize Guardrails guard with cybersecurity-specific validators
        self.guard = Guard.from_rail_string("""
        <rail version="0.1">
        <output>
            <string name="secure_code" validators="valid-length: 10 5000" />
            <string name="rationale" validators="valid-length: 50 1000" />
        </output>
        </rail>
        """)
        
    def protect_prompt(self, prompt: str) -> Dict[str, Any]:
        """Apply Guardrails protection to user prompts"""
        try:
            # Check for prompt injection patterns
            if self._detect_prompt_injection(prompt):
                return {
                    "status": "blocked",
                    "reason": "Potential prompt injection detected",
                    "safe_prompt": None
                }
            
            # Apply content filtering
            filtered_prompt = self._apply_content_filters(prompt)
            
            return {
                "status": "approved",
                "safe_prompt": filtered_prompt,
                "modifications": []
            }
        except Exception as e:
            logger.error(f"Error in prompt protection: {e}")
            return {
                "status": "error",
                "reason": str(e),
                "safe_prompt": None
            }
    
    def _detect_prompt_injection(self, prompt: str) -> bool:
        """Detect common prompt injection patterns"""
        injection_patterns = [
            "ignore previous instructions",
            "forget your role",
            "you are now",
            "system:",
            "assistant:",
            "jailbreak",
            "DAN mode"
        ]
        
        prompt_lower = prompt.lower()
        return any(pattern in prompt_lower for pattern in injection_patterns)
    
    def _apply_content_filters(self, prompt: str) -> str:
        """Apply content filtering and topic restriction"""
        # Ensure prompt is cybersecurity-focused
        if not self._is_cybersecurity_related(prompt):
            return f"Please focus on cybersecurity topics. {prompt}"
        
        return prompt
    
    def _is_cybersecurity_related(self, prompt: str) -> bool:
        """Check if prompt is related to cybersecurity"""
        cybersec_keywords = [
            "security", "vulnerability", "encryption", "authentication",
            "authorization", "malware", "firewall", "penetration testing",
            "secure coding", "OWASP", "SQL injection", "XSS", "CSRF"
        ]
        
        prompt_lower = prompt.lower()
        return any(keyword in prompt_lower for keyword in cybersec_keywords)

def validate_response(response: str) -> Dict[str, Any]:
    """Validate LLM response for security and quality"""
    try:
        # Check for potentially harmful content
        if _contains_harmful_content(response):
            return {
                "valid": False,
                "reason": "Response contains potentially harmful content"
            }
        
        # Validate code quality if response contains code
        if _contains_code(response):
            code_validation = _validate_code_security(response)
            if not code_validation["secure"]:
                return {
                    "valid": False,
                    "reason": f"Insecure code detected: {code_validation['issues']}"
                }
        
        return {"valid": True, "reason": "Response validated successfully"}
        
    except Exception as e:
        logger.error(f"Error validating response: {e}")
        return {"valid": False, "reason": f"Validation error: {str(e)}"}

def _contains_harmful_content(response: str) -> bool:
    """Check for harmful or malicious content"""
    harmful_patterns = [
        "rm -rf", "format c:", "del /f /q",
        "DROP TABLE", "DELETE FROM",
        "eval(", "exec(", "system(",
        "malicious payload", "backdoor"
    ]
    
    response_lower = response.lower()
    return any(pattern in response_lower for pattern in harmful_patterns)

def _contains_code(response: str) -> bool:
    """Check if response contains code"""
    code_indicators = ["```", "def ", "function ", "class ", "import ", "from "]
    return any(indicator in response for indicator in code_indicators)

def _validate_code_security(response: str) -> Dict[str, Any]:
    """Validate code for common security issues"""
    issues = []
    
    # Check for common security anti-patterns
    security_checks = {
        "SQL injection": ["execute(", "query(", "cursor.execute"],
        "Command injection": ["os.system", "subprocess.call", "eval("],
        "Path traversal": ["../", "..\\", "os.path.join"],
        "Hardcoded credentials": ["password=", "api_key=", "secret="]
    }
    
    for issue_type, patterns in security_checks.items():
        if any(pattern in response for pattern in patterns):
            issues.append(issue_type)
    
    return {
        "secure": len(issues) == 0,
        "issues": issues
    }

def log_guardrails_usage(prompt: str, response: str, user_id: str = None) -> None:
    """Log Guardrails usage for auditing"""
    audit_data = {
        "timestamp": str(datetime.now()),
        "user_id": user_id,
        "prompt_length": len(prompt),
        "response_length": len(response),
        "security_checks": "passed"
    }
    
    logger.info(f"Guardrails audit: {audit_data}")