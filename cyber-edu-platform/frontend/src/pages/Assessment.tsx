import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Assessment = () => {
    const [assessments, setAssessments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchAssessments = async () => {
            try {
                const response = await axios.get('/api/assessments');
                setAssessments(response.data);
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        };

        fetchAssessments();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error loading assessments: {error.message}</div>;

    return (
        <div>
            <h1>Assessments</h1>
            <ul>
                {assessments.map((assessment) => (
                    <li key={assessment.id}>
                        <h2>{assessment.title}</h2>
                        <p>{assessment.description}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Assessment;