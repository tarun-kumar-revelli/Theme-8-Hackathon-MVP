import React, { useState } from 'react';

const Editor: React.FC = () => {
    const [code, setCode] = useState<string>('');

    const handleCodeChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        setCode(event.target.value);
    };

    return (
        <div className="editor-container">
            <h2>Code Editor</h2>
            <textarea
                value={code}
                onChange={handleCodeChange}
                rows={10}
                cols={50}
                placeholder="Write your code here..."
            />
        </div>
    );
};

export default Editor;