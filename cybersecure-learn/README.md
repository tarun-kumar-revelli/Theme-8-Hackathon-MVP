# CyberSecure Learn - MVP for Secure Coding Tutor

## Overview
CyberSecure Learn is a Minimum Viable Product (MVP) designed to provide an interactive learning experience for secure coding practices. Powered by LLMs, this application analyzes user-submitted code, identifies vulnerabilities based on the OWASP Top 10, and offers AI-driven feedback and secure coding alternatives.

## Project Structure
The project is divided into two main parts: the backend and the frontend.

### Backend
- **FastAPI** application that handles API requests and responses.
- **Endpoints** for code submission and analysis.
- **Security utilities** for validating and sanitizing user input.

### Frontend
- **React** application that provides a user-friendly interface for code submission and displaying analysis results.
- Components for inputting code and viewing feedback.

## Features
- Accepts user-submitted code via the frontend.
- Analyzes code for vulnerabilities using GPT-4.
- Provides explanations and suggestions for secure coding practices.
- Clean and responsive UI with loading states and error handling.

## Setup Instructions

### Backend
1. Navigate to the `backend` directory.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file from the `.env.template` and add your OpenAI API key.
4. Run the FastAPI application:
   ```
   uvicorn src.main:app --reload
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Install dependencies:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Future Enhancements
- Integration of quizzes and assessments to reinforce learning.
- Expansion of the vulnerability database with real-time updates.
- User authentication and progress tracking.

## License
This project is licensed under the MIT License. See the LICENSE file for details.