/** @format */

import React from "react";
import { HashRouter as Router } from "react-router-dom";
import Routes from "./routes";
import history from "./services/history";
function App() {
  return (
    <Router history={history}>
      <Routes />
    </Router>
  );
}

export default App;
