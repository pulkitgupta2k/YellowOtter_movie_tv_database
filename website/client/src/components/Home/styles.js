import styled from "styled-components";

export const HomeDefaultContainer = styled.div`
  height: 90vh;
  // background:#010913;
  background: url(../../images/bg.jpg);
  //   background: var(--main-blue);
`;
export const HomeContainer = styled.div`
  display: flex;
  flex-flow: row wrap;
  align-content: center;
  justify-content: center;
  min-height: 30vh;
  padding: 5rem 0 5rem 0;
  .left {
    width: 40%;
    margin-right: 2rem;
  }
  .right {
    width: 40%;
    margin-left: 2rem;
  }
  .title {
    color: white;
    font-size: 4rem;
    font-weight: 600;
    padding: 0;
    margin: 0;
  }
  .title2 {
    color: white;
    font-size: 3rem;
    font-weight: 600;
    padding: 0;
    margin: 0;
    width: 80%;
  }
  .title3 {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 500;
    width: 50%;
    align-self: center;
  }
  .subtitle {
    font-size: x-large;
    color: var(--main-grey);
  }
  .pretitle {
    font-size: large;
    color: var(--main-yellow);
    text-shadow: 4px 4px 0 8px rgba(244, 192, 1, 0.6);
  }
  .tv {
    height: 30rem;
  }
  .logo {
    height: 4rem;
  }
  .container2 {
    display: flex;
    flex-direction: column;
    text-align: center;
    justify-content: center;
    align-content: center;
  }
`;
