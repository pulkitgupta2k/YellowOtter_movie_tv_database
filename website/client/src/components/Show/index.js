import React from "react";
import styled from "styled-components";

import image1 from "../../images/show1.jfif";
import image2 from "../../images/show1_1.jfif";
import logo from "../../images/yos.jfif";

export default function ShowComponent() {
  return (
    <ShowContainer>
      <HeaderShow>
        <img src={image1} alt="lala" />
      </HeaderShow>
      <MainShow>
        <div className="main-img">
          <img src={image2} alt="lala" />
          <p className="side-info">
            RATING:{" "}
            <img
              alt="lala"
              src={logo}
              style={{
                height: "48px",
                width: "48px",
                borderRadius: "0",
                boxShadow: "none",
              }}
            />{" "}
            80%
            <br />
            GENRES: DRAMA
          </p>
        </div>
        <div className="main-info">
          <p className="title">I MAY DESTROY YOU - SEASON ONE</p>
          <p className="text-info">12 EPISODES</p>
          <div className="episode">
            <p className="episode-text">S1 E1 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E2 - Someone Is Lying</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E3 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E4 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E5 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E6 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E7 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E8 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E9 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E10 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E11 - EYES EYES EYES</p>
          </div>
          <div className="episode">
            <p className="episode-text">S1 E12 - EYES EYES EYES</p>
          </div>
        </div>
      </MainShow>
    </ShowContainer>
  );
}

const ShowContainer = styled.div`
  display: flex;
  flex-direction: column;
`;

const HeaderShow = styled.div`
  width: 100%;
  object-fit: stretch;
  align-self: center;
  z-index: 1;
  img {
    width: 100%;
    height: 100%;
    position: fixed;
    // top:0;
    // z-index:-1;
  }
`;

const MainShow = styled.div`
  z-index: 10;
  min-height: 100vh;
  width: 80vw;
  align-self: center;
  margin-top: 15rem;
  border-top-left-radius: 24px;
  border-top-right-radius: 24px;
  border: 10px solid var(--main-blue);
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;

  .main-img {
    width: 25%;
    margin: 5rem 2rem 0 2rem;
  }
  .side-info {
    border-top: 2px solid var(--main-blue);
    border-bottom: 2px solid var(--main-blue);
    padding-top: 2rem;
    padding-bottom: 2rem;
    color: var(--main-yellow);
    font-size: x-large;
  }
  img {
    width: 100%;
    object-fit: cover;
    border-radius: 24px;
    box-shadow: 4px 4px 8px 0px rgba(255, 255, 255, 0.2);
  }
  .main-info {
    width: 60%;
    margin: 4rem 0 0 0;
  }
  .title {
    font-size: xx-large;
    color: var(--main-yellow);
  }
  .text-info {
    font-size: large;
    color: var(--main-grey);
  }
  .episode {
    padding: 0.25rem 0 0.25rem 0;
    border-bottom: 2px solid var(--main-blue);
    width: 100%;
  }
  .episode-text {
    color: white;
    padding-left: 1rem;
  }
`;
