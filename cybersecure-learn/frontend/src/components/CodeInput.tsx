import React, { useState } from 'react';

const CodeInput: React.FC<{ onSubmit: (code: string) => void }> = ({ onSubmit }) => {
    const [code, setCode] = useState('');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        onSubmit(code);
        setCode('');
    };

    return (
        <form onSubmit={handleSubmit} className="code-input-form">
            <textarea
                value={code}
                onChange={(e) => setCode(e.target.value)}
                placeholder="Enter your code here..."
                className="code-input"
                rows={10}
                required
            />
            <button type="submit" className="submit-button">Analyze Code</button>
        </form>
    );
};

export default CodeInput;