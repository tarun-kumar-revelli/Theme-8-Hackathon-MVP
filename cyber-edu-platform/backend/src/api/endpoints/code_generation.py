from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.guardrails import generate_code_with_guardrails

router = APIRouter()

class CodeGenerationRequest(BaseModel):
    prompt: str

class CodeGenerationResponse(BaseModel):
    generated_code: str

@router.post("/generate-code", response_model=CodeGenerationResponse)
async def generate_code(request: CodeGenerationRequest):
    try:
        generated_code = await generate_code_with_guardrails(request.prompt)
        return CodeGenerationResponse(generated_code=generated_code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))