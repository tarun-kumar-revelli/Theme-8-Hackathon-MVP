import React, { useState } from 'react';
import { getExplanation } from '@services/api';

interface ExplanationData {
  explanation: string;
  security_assessment: {
    level: string;
    issues: string[];
    recommendations: string[];
  };
  references: {
    title: string;
    url: string;
    source: string;
  }[];
  owasp_guidelines: string[];
  transparency_info: {
    model_used: string;
    confidence_score: number;
    generation_timestamp: string;
  };
}

const ExplainabilityModule: React.FC<{ code: string }> = ({ code }) => {
  const [explanation, setExplanation] = useState<ExplanationData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleExplain = async () => {
    setLoading(true);
    setError(null);
    
    try {
      const response = await getExplanation(code);
      setExplanation(response.data);
    } catch (err) {
      setError('Failed to generate explanation');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="explainability-module bg-white rounded-lg shadow-md p-6">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold text-gray-800">Code Explanation & Security Analysis</h3>
        <button
          onClick={handleExplain}
          disabled={loading || !code.trim()}
          className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 disabled:opacity-50"
        >
          {loading ? 'Analyzing...' : 'Explain Code'}
        </button>
      </div>

      {error && (
        <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
          {error}
        </div>
      )}

      {explanation && (
        <div className="space-y-6">
          {/* Main Explanation */}
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="font-semibold mb-2">Explanation</h4>
            <p className="text-gray-700 whitespace-pre-wrap">{explanation.explanation}</p>
          </div>

          {/* Security Assessment */}
          <div className="grid md:grid-cols-2 gap-4">
            <div className="bg-yellow-50 p-4 rounded-lg">
              <h4 className="font-semibold mb-2 text-yellow-800">Security Assessment</h4>
              <div className="space-y-2">
                <p><span className="font-medium">Level:</span> 
                  <span className={`ml-2 px-2 py-1 rounded text-xs ${
                    explanation.security_assessment.level === 'High' ? 'bg-red-100 text-red-800' :
                    explanation.security_assessment.level === 'Medium' ? 'bg-yellow-100 text-yellow-800' :
                    'bg-green-100 text-green-800'
                  }`}>
                    {explanation.security_assessment.level}
                  </span>
                </p>
                {explanation.security_assessment.issues.length > 0 && (
                  <div>
                    <p className="font-medium">Issues Found:</p>
                    <ul className="list-disc list-inside text-sm text-gray-600">
                      {explanation.security_assessment.issues.map((issue, index) => (
                        <li key={index}>{issue}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>

            <div className="bg-blue-50 p-4 rounded-lg">
              <h4 className="font-semibold mb-2 text-blue-800">Recommendations</h4>
              <ul className="list-disc list-inside text-sm text-gray-600 space-y-1">
                {explanation.security_assessment.recommendations.map((rec, index) => (
                  <li key={index}>{rec}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* OWASP Guidelines */}
          {explanation.owasp_guidelines.length > 0 && (
            <div className="bg-green-50 p-4 rounded-lg">
              <h4 className="font-semibold mb-2 text-green-800">Related OWASP Guidelines</h4>
              <div className="flex flex-wrap gap-2">
                {explanation.owasp_guidelines.map((guideline, index) => (
                  <span key={index} className="bg-green-100 text-green-800 px-2 py-1 rounded text-xs">
                    {guideline}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* References */}
          <div className="bg-gray-50 p-4 rounded-lg">
            <h4 className="font-semibold mb-2">References & Sources</h4>
            <div className="space-y-2">
              {explanation.references.map((ref, index) => (
                <div key={index} className="border-l-4 border-blue-500 pl-3">
                  <a
                    href={ref.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-600 hover:underline font-medium"
                  >
                    {ref.title}
                  </a>
                  <p className="text-sm text-gray-600">{ref.source}</p>
                </div>
              ))}
            </div>
          </div>

          {/* Transparency Information */}
          <div className="bg-gray-100 p-3 rounded text-sm text-gray-600">
            <h5 className="font-medium mb-1">Transparency Information</h5>
            <p>Model: {explanation.transparency_info.model_used}</p>
            <p>Confidence: {(explanation.transparency_info.confidence_score * 100).toFixed(1)}%</p>
            <p>Generated: {new Date(explanation.transparency_info.generation_timestamp).toLocaleString()}</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default ExplainabilityModule;