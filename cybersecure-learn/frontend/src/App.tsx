import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Analysis from './pages/Analysis';
import CodeInput from './components/CodeInput';
import ResultsDisplay from './components/ResultsDisplay';

const App: React.FC = () => {
  return (
    <Router>
      <div className="app">
        <h1>CyberSecure Learn</h1>
        <CodeInput />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/analysis" component={Analysis} />
        </Switch>
        <ResultsDisplay />
      </div>
    </Router>
  );
};

export default App;