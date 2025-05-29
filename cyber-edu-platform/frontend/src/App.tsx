import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import CodeAssistant from './pages/CodeAssistant';
import Scenarios from './pages/Scenarios';
import Assessment from './pages/Assessment';
import Editor from './components/Editor';
import Simulator from './components/Simulator';
import Dashboard from './components/Dashboard';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={CodeAssistant} />
        <Route path="/scenarios" component={Scenarios} />
        <Route path="/assessment" component={Assessment} />
        <Route path="/editor" component={Editor} />
        <Route path="/simulator" component={Simulator} />
        <Route path="/dashboard" component={Dashboard} />
      </Switch>
    </Router>
  );
};

export default App;