/** @format */

import React from "react";
import { Switch } from "react-router-dom";
import Route from "./Route";

//importing the components, lol ok

import Home from "../pages/Home";
import Show from "../pages/Show";
import Nav from "../components/Nav";
import NewPage from "../pages/NewPage";

const Routes = () => {
  return (
    <div style={{ overflowX: "hidden" }}>
      <Nav />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/new" component={NewPage} />
        <Route exact path="/show" component={Show} />
      </Switch>
    </div>
  );
};

export default Routes;
