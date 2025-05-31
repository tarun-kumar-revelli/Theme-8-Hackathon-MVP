from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
import torch
from typing import Dict, List, Optional
import json
from .guardrails import SecurityGuard, validate_response
from ..core.config import Config
import logging

logger = logging.getLogger(__name__)

class CybersecurityLLM:
    def __init__(self):
        self.config = Config()
        self.security_guard = SecurityGuard()
        self.model = None
        self.tokenizer = None
        self._load_model()
    
    def _load_model(self):
        """Load fine-tuned model or base model"""
        try:
            model_name = self.config.MODEL_NAME
            if self.config.USE_FINE_TUNED_MODEL:
                # Load fine-tuned model for cybersecurity
                model_path = f"{self.config.MODEL_PATH}/cybersec-fine-tuned"
                self.tokenizer = AutoTokenizer.from_pretrained(model_path)
                self.model = AutoModelForCausalLM.from_pretrained(
                    model_path,
                    torch_dtype=torch.float16,
                    device_map="auto"
                )
            else:
                # Use base model with cybersecurity prompt engineering
                self.tokenizer = AutoTokenizer.from_pretrained(model_name)
                self.model = AutoModelForCausalLM.from_pretrained(
                    model_name,
                    torch_dtype=torch.float16,
                    device_map="auto"
                )
            
            logger.info(f"Model loaded successfully: {model_name}")
            
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            raise

def generate_code(prompt: str, user_id: str = None) -> Dict[str, Any]:
    """Generate secure code with guardrails protection"""
    try:
        llm = CybersecurityLLM()
        
        # Apply security protection to prompt
        prompt_check = llm.security_guard.protect_prompt(prompt)
        
        if prompt_check["status"] != "approved":
            return {
                "generated_code": None,
                "rationale": f"Prompt blocked: {prompt_check['reason']}",
                "security_status": "blocked",
                "references": []
            }
        
        safe_prompt = prompt_check["safe_prompt"]
        
        # Enhance prompt with cybersecurity context
        enhanced_prompt = f"""
        You are a cybersecurity expert assistant. Generate secure code following OWASP guidelines.
        
        User request: {safe_prompt}
        
        Requirements:
        1. Follow secure coding practices
        2. Include input validation
        3. Implement proper error handling
        4. Use parameterized queries for database operations
        5. Include security comments explaining the approach
        
        Provide both code and explanation:
        """
        
        # Generate response using the model
        inputs = llm.tokenizer.encode(enhanced_prompt, return_tensors="pt")
        
        with torch.no_grad():
            outputs = llm.model.generate(
                inputs,
                max_length=1024,
                temperature=0.7,
                do_sample=True,
                pad_token_id=llm.tokenizer.eos_token_id
            )
        
        generated_text = llm.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract code and rationale
        response_parts = _parse_response(generated_text)
        
        # Validate response
        validation = validate_response(response_parts["code"])
        
        if not validation["valid"]:
            return {
                "generated_code": None,
                "rationale": f"Generated code failed security validation: {validation['reason']}",
                "security_status": "validation_failed",
                "references": []
            }
        
        # Add security references
        references = _get_security_references(prompt)
        
        return {
            "generated_code": response_parts["code"],
            "rationale": response_parts["rationale"],
            "security_status": "approved",
            "references": references,
            "owasp_guidelines": _get_relevant_owasp_guidelines(prompt)
        }
        
    except Exception as e:
        logger.error(f"Error generating code: {e}")
        return {
            "generated_code": None,
            "rationale": f"Error generating code: {str(e)}",
            "security_status": "error",
            "references": []
        }

def simulate_threat_scenario(scenario_type: str = "random") -> Dict[str, Any]:
    """Generate realistic threat simulation scenarios"""
    
    scenarios_db = {
        "sql_injection": {
            "id": "sql_injection_001",
            "title": "SQL Injection in User Authentication",
            "description": "A web application vulnerability where user input is directly concatenated into SQL queries",
            "threat_level": "High",
            "attack_vector": "Web Application",
            "vulnerable_code": """
            def authenticate_user(username, password):
                query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
                cursor.execute(query)
                return cursor.fetchone()
            """,
            "exploit_example": "admin' OR '1'='1' --",
            "impact": "Complete database compromise, unauthorized access",
            "mitigation_steps": [
                "Use parameterized queries",
                "Implement input validation",
                "Apply principle of least privilege",
                "Use stored procedures"
            ],
            "owasp_category": "A03:2021 – Injection",
            "cwe_id": "CWE-89",
            "learning_objectives": [
                "Understand SQL injection mechanics",
                "Learn parameterized query implementation",
                "Practice input validation techniques"
            ]
        },
        "xss": {
            "id": "xss_001",
            "title": "Cross-Site Scripting (XSS) Attack",
            "description": "Reflected XSS vulnerability in search functionality",
            "threat_level": "Medium",
            "attack_vector": "Web Browser",
            "vulnerable_code": """
            def search_results(query):
                return f"<h1>Search results for: {query}</h1>"
            """,
            "exploit_example": "<script>alert('XSS')</script>",
            "impact": "Session hijacking, credential theft, defacement",
            "mitigation_steps": [
                "HTML encode user input",
                "Implement Content Security Policy",
                "Use secure templating engines",
                "Validate and sanitize input"
            ],
            "owasp_category": "A03:2021 – Injection",
            "cwe_id": "CWE-79"
        }
    }
    
    if scenario_type == "random":
        import random
        scenario_key = random.choice(list(scenarios_db.keys()))
    else:
        scenario_key = scenario_type if scenario_type in scenarios_db else "sql_injection"
    
    scenario = scenarios_db[scenario_key]
    scenario["interactive_elements"] = _generate_interactive_elements(scenario)
    
    return scenario

def assess_code_submission(submission: str, scenario_id: str, user_id: str = None) -> Dict[str, Any]:
    """Evaluate submitted code for secure coding practices"""
    
    try:
        # Load assessment criteria for the specific scenario
        criteria = _load_assessment_criteria(scenario_id)
        
        # Analyze the submission
        analysis_results = _analyze_code_security(submission, criteria)
        
        # Calculate score based on OWASP Top 10 compliance
        score = _calculate_owasp_score(analysis_results)
        
        # Generate detailed feedback
        feedback = _generate_detailed_feedback(analysis_results, criteria)
        
        # Track assessment for benchmarking
        _log_assessment_result(user_id, scenario_id, score, analysis_results)
        
        return {
            "score": score,
            "max_score": 100,
            "feedback": feedback,
            "security_analysis": analysis_results,
            "improvement_suggestions": _get_improvement_suggestions(analysis_results),
            "owasp_compliance": _check_owasp_compliance(submission),
            "benchmarks": _get_benchmark_comparison(score, scenario_id)
        }
        
    except Exception as e:
        logger.error(f"Error assessing code submission: {e}")
        return {
            "score": 0,
            "feedback": f"Assessment failed: {str(e)}",
            "error": True
        }

def explain_code(code: str, context: str = None) -> Dict[str, Any]:
    """Provide detailed explanation with security focus and references"""
    
    try:
        llm = CybersecurityLLM()
        
        explanation_prompt = f"""
        As a cybersecurity expert, explain the following code with focus on:
        1. Security implications
        2. Potential vulnerabilities
        3. Best practices compliance
        4. OWASP guideline alignment
        
        Code to explain:
        {code}
        
        Context: {context or 'General security review'}
        
        Provide structured explanation with references.
        """
        
        # Generate explanation
        inputs = llm.tokenizer.encode(explanation_prompt, return_tensors="pt")
        
        with torch.no_grad():
            outputs = llm.model.generate(
                inputs,
                max_length=1024,
                temperature=0.3,  # Lower temperature for more focused explanations
                do_sample=True,
                pad_token_id=llm.tokenizer.eos_token_id
            )
        
        explanation_text = llm.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Parse and structure the explanation
        structured_explanation = _structure_explanation(explanation_text)
        
        # Add authoritative references
        references = _get_authoritative_references(code)
        
        return {
            "explanation": structured_explanation,
            "security_assessment": _assess_code_security_level(code),
            "references": references,
            "related_owasp_guidelines": _map_to_owasp_guidelines(code),
            "learning_resources": _get_learning_resources(code),
            "transparency_info": {
                "model_used": llm.config.MODEL_NAME,
                "confidence_score": _calculate_explanation_confidence(code),
                "generation_timestamp": str(datetime.now())
            }
        }
        
    except Exception as e:
        logger.error(f"Error explaining code: {e}")
        return {
            "explanation": f"Error generating explanation: {str(e)}",
            "error": True
        }

# Helper functions
def _parse_response(generated_text: str) -> Dict[str, str]:
    """Parse generated response into code and rationale"""
    # Implementation to extract code blocks and explanations
    pass

def _get_security_references(prompt: str) -> List[str]:
    """Get relevant security references based on prompt"""
    # Implementation to return relevant OWASP, NIST references
    pass

def _load_assessment_criteria(scenario_id: str) -> Dict:
    """Load assessment criteria for specific scenario"""
    # Implementation to load scenario-specific criteria
    pass

def _analyze_code_security(code: str, criteria: Dict) -> Dict:
    """Analyze code for security issues"""
    # Implementation for security analysis
    pass

def _calculate_owasp_score(analysis: Dict) -> float:
    """Calculate score based on OWASP compliance"""
    # Implementation for OWASP-based scoring
    pass