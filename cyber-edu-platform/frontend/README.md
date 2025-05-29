# frontend/README.md

# Cybersecurity Education Platform - Frontend

Welcome to the frontend of the Cybersecurity Education Platform! This platform is designed to provide practical, interactive web-based education on secure coding and cybersecurity concepts using Large Language Models (LLMs).

## Project Structure

- **src/**: Contains the source code for the React application.
  - **components/**: Reusable components for the application.
    - `Editor.tsx`: Code editor component for the platform.
    - `Simulator.tsx`: Scenario simulator component.
    - `Dashboard.tsx`: Assessment dashboard component.
  - **pages/**: Contains the main pages of the application.
    - `CodeAssistant.tsx`: Page for the code assistant.
    - `Scenarios.tsx`: Page for scenarios.
    - `Assessment.tsx`: Page for assessments.
  - **services/**: Functions for connecting to the backend via REST API.
    - `api.ts`: API service functions.
  - **types/**: TypeScript types used throughout the frontend.
    - `index.ts`: Type definitions.
  - `App.tsx`: Main application component.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd cyber-edu-platform/frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the application**:
   ```bash
   npm start
   ```

## Features

- Code assistant with an integrated editor.
- Interactive scenario simulator for threat simulations.
- Assessment dashboard for tracking scores and feedback.
- Responsive design using Tailwind CSS.

## Contributing

We welcome contributions! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.