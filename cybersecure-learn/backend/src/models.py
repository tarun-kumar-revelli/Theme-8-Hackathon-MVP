from pydantic import BaseModel
from typing import List, Optional

class CodeAnalysisRequest(BaseModel):
    code: str
    language: str

class Vulnerability(BaseModel):
    type: str
    description: str
    suggestion: str

class CodeAnalysisResponse(BaseModel):
    vulnerabilities: List[Vulnerability]
    fixed_code: Optional[str] = None
    message: Optional[str] = None