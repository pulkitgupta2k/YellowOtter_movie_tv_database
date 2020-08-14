/** @format */

import React from "react";
import { NavContainer, NavSubContainer } from "./styles";

function Nav() {
  return (
    <NavContainer>
      <NavSubContainer>
        <ul className="nav-links">
          <li>Home</li>
          <li>New</li>
          <li>Popular</li>
          <li>Movies</li>
          <li>Tv Series</li>
        </ul>
        <input placeholder="Search for movies or tv shows" />
      </NavSubContainer>
    </NavContainer>
  );
}

export default Nav;
