from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.endpoints import code_generation, scenarios, assessments, explanations

app = FastAPI(title="Cybersecurity Education Platform API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(code_generation.router, prefix="/api/code", tags=["Code Generation"])
app.include_router(scenarios.router, prefix="/api/scenarios", tags=["Scenarios"])
app.include_router(assessments.router, prefix="/api/assessments", tags=["Assessments"])
app.include_router(explanations.router, prefix="/api/explanations", tags=["Explanations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cybersecurity Education Platform API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}