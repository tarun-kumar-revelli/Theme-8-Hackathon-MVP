from fastapi import APIRouter

router = APIRouter()

@router.get("/simulate-scenario")
async def simulate_scenario():
    """
    Returns a threat simulation scenario.
    """
    # Placeholder for threat simulation logic
    scenario = {
        "id": 1,
        "title": "SQL Injection Attack",
        "description": "A scenario where an attacker attempts to execute arbitrary SQL code on a database."
    }
    return scenario