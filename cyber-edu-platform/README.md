# README.md for Cybersecurity Education Platform

# Cybersecurity Education Platform

Welcome to the Cybersecurity Education Platform, a practical, interactive web-based platform designed to teach secure coding and cybersecurity concepts using Large Language Models (LLMs). This platform aims to provide an engaging learning experience through various components, including a code assistant, scenario simulator, assessment engine, and an explainability module.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

The backend is built using FastAPI and includes the following features:

- **API Endpoints**: 
  - `/generate-code`: LLM-secured code generation with prompt injection protection.
  - `/simulate-scenario`: Returns a threat simulation scenario.
  - `/submit-assessment`: Submits and scores secure coding exercises.
  - `/explain-output`: Provides LLM-powered rationale with source references.

- **Middleware**: 
  - Logging for security audits.
  - Request validation.

- **Core Components**: 
  - Configuration settings for loading datasets and fine-tuned models.
  - Security-related functions.

- **Testing**: Unit tests to ensure the reliability of the backend services.

### Frontend

The frontend is developed using React.js and includes:

- **Components**: 
  - Code editor for the code assistant.
  - Scenario simulator for interactive quizzes.
  - Assessment dashboard for scores and feedback.

- **Pages**: 
  - Code Assistant
  - Scenarios
  - Assessment

- **Styling**: Utilizes Tailwind CSS for a modern and responsive design.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd cyber-edu-platform
   ```

2. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the FastAPI server:
     ```bash
     uvicorn src.main:app --reload
     ```

3. **Frontend Setup**:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the React application:
     ```bash
     npm start
     ```

4. **Docker Setup** (Optional):
   - Use Docker to run the entire application stack:
     ```bash
     docker-compose up
     ```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Thank you for your interest in the Cybersecurity Education Platform! We hope you find it useful in your learning journey.