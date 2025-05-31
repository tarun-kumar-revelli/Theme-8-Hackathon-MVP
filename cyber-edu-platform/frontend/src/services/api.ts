import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const generateCode = async (prompt: string) => {
    const response = await axios.post(`${API_BASE_URL}/api/code/generate-code`, { prompt });
    return response;
};

export const getScenario = async () => {
    const response = await axios.get(`${API_BASE_URL}/api/scenarios/simulate-scenario`);
    return response;
};

export const submitAssessment = async (assessmentData: any) => {
    const response = await axios.post(`${API_BASE_URL}/api/assessments/submit`, assessmentData);
    return response;
};

export const getExplanation = async (code: string) => {
    const response = await axios.post(`${API_BASE_URL}/api/explanations/explain`, { code });
    return response;
};