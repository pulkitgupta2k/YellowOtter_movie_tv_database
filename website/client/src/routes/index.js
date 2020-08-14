/** @format */

import React from "react";
import { Switch } from "react-router-dom";
import Route from "./Route";

//importing the components
import Nav from "../components/Nav";
import Home from "../pages/Home";
import Show from "../pages/Show";

const Routes = () => {
  return (
    <>
      <Nav />
      <Switch>
        <Route exact path="/show" component={Show} />
        <Route exact path="/" component={Home} />
      </Switch>
    </>
  );
};

export default Routes;
