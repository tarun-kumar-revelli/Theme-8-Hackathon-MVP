import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

export const generateCode = async (prompt) => {
    const response = await axios.post(`${API_BASE_URL}/generate-code`, { prompt });
    return response.data;
};

export const getScenario = async () => {
    const response = await axios.get(`${API_BASE_URL}/generate-scenario`);
    return response.data;
};

export const submitAssessment = async (assessmentData) => {
    const response = await axios.post(`${API_BASE_URL}/submit-assessment`, assessmentData);
    return response.data;
};

export const getExplanation = async (code) => {
    const response = await axios.post(`${API_BASE_URL}/explain-output`, { code });
    return response.data;
};