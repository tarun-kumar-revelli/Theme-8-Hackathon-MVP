from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .prompts import build_prompt
from .rag import get_stubbed_response
from .models import CodeAnalysisRequest, CodeAnalysisResponse

app = FastAPI()

# Allow CORS for all origins (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze-code", response_model=CodeAnalysisResponse)
async def analyze_code(request: CodeAnalysisRequest):
    user_code = request.code
    prompt = build_prompt(user_code)
    response = get_stubbed_response(prompt)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)