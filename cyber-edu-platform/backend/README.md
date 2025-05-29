# README for Cybersecurity Education Platform Backend

## Overview
This backend is part of the Cybersecurity Education Platform, designed to provide a practical, interactive web-based environment for teaching secure coding and cybersecurity concepts using Large Language Models (LLMs).

## Features
- **LLM-Secured Code Generation**: An endpoint for generating code with prompt injection protection.
- **Threat Simulation Scenarios**: An endpoint to return various threat simulation scenarios.
- **Secure Coding Assessments**: An endpoint to submit and score secure coding exercises.
- **Explainability**: An endpoint that provides LLM-powered rationale with source references.

## Directory Structure
```
backend/
├── src/
│   ├── api/
│   │   ├── endpoints/
│   │   ├── middleware/
│   │   └── __init__.py
│   ├── core/
│   ├── models/
│   ├── services/
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository.
2. Navigate to the `backend` directory.
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the FastAPI application:
   ```
   uvicorn src.main:app --reload
   ```

## API Documentation
Refer to the FastAPI auto-generated documentation at `http://localhost:8000/docs` for details on available endpoints and their usage.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.