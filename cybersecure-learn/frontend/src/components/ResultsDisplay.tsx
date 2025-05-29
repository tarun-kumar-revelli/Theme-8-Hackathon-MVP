import React from 'react';

interface ResultsDisplayProps {
    vulnerabilities: Array<{
        id: string;
        description: string;
        suggestion: string;
    }>;
    loading: boolean;
    error: string | null;
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ vulnerabilities, loading, error }) => {
    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    return (
        <div>
            <h2>Analysis Results</h2>
            {vulnerabilities.length === 0 ? (
                <p>No vulnerabilities found.</p>
            ) : (
                <ul>
                    {vulnerabilities.map(vuln => (
                        <li key={vuln.id}>
                            <strong>{vuln.description}</strong>
                            <p>Suggestion: {vuln.suggestion}</p>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default ResultsDisplay;