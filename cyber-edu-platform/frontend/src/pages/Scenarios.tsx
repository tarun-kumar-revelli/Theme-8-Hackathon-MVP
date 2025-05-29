import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Scenarios = () => {
    const [scenarios, setScenarios] = useState([]);

    useEffect(() => {
        const fetchScenarios = async () => {
            try {
                const response = await axios.get('/api/scenarios');
                setScenarios(response.data);
            } catch (error) {
                console.error('Error fetching scenarios:', error);
            }
        };

        fetchScenarios();
    }, []);

    return (
        <div>
            <h1>Threat Simulation Scenarios</h1>
            <ul>
                {scenarios.map((scenario) => (
                    <li key={scenario.id}>{scenario.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default Scenarios;