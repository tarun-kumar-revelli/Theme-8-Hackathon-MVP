import React from 'react';

const Home: React.FC = () => {
    return (
        <div className="flex flex-col items-center justify-center h-screen">
            <h1 className="text-4xl font-bold mb-4">Welcome to CyberSecure Learn</h1>
            <p className="text-lg mb-8">Your interactive secure coding tutor powered by AI.</p>
            <a href="/code-input" className="bg-blue-500 text-white px-4 py-2 rounded">
                Get Started
            </a>
        </div>
    );
};

export default Home;