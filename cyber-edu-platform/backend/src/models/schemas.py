from pydantic import BaseModel
from typing import List, Optional

class CodeGenerationRequest(BaseModel):
    prompt: str
    user_id: str

class CodeGenerationResponse(BaseModel):
    generated_code: str
    rationale: Optional[str]

class ThreatScenario(BaseModel):
    scenario_id: str
    description: str
    impact: str
    mitigation: List[str]

class AssessmentSubmission(BaseModel):
    user_id: str
    code: str
    scenario_id: str

class AssessmentResult(BaseModel):
    score: float
    feedback: str

class ExplanationRequest(BaseModel):
    code: str
    user_id: str

class ExplanationResponse(BaseModel):
    rationale: str
    references: List[str]