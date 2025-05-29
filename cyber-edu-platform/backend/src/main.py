from fastapi import FastAPI
from api.endpoints import code_generation, scenarios, assessments, explanations
from api.middleware import audit, validation

app = FastAPI()

# Include middleware
app.add_middleware(audit.AuditMiddleware)
app.add_middleware(validation.ValidationMiddleware)

# Include API routes
app.include_router(code_generation.router, prefix="/api/code", tags=["Code Generation"])
app.include_router(scenarios.router, prefix="/api/scenarios", tags=["Scenarios"])
app.include_router(assessments.router, prefix="/api/assessments", tags=["Assessments"])
app.include_router(explanations.router, prefix="/api/explanations", tags=["Explanations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cybersecurity Education Platform API"}