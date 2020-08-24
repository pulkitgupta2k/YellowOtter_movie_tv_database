/** @format */
import styled from "styled-components";
export const NavContainer = styled.div`
  display: flex;
  background: black;
  height: 10vh;
  z-index: 99;
  position: fixed;
  width: 100%;
`;

export const NavSubContainer = styled.div`
  width: 80%;
  margin: auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  .nav-links {
    display: flex;
    list-style: none;
    justify-content: space-between;

    li {
      text-transform: uppercase;
      color: grey;
      margin-right: 20px;
      &:hover {
        color: white;
        cursor: pointer;
      }
    }
  }
  input {
    outline: none;
    border: none;
    border-bottom: 1px solid grey;
    padding: 2px;
    margin: 0;
    height: fit-content;
    width: 30vw;
  }
`;
