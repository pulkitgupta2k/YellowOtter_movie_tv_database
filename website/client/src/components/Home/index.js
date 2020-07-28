import React from 'react';

import styled from 'styled-components';
import { HomeContainer, HomeDefaultContainer } from "./styles";

import image1 from '../../images/tab-tv.png';
import image2 from '../../images/tab-macbook.png';
import image3 from '../../images/tab-tablet.png';
import image4 from '../../images/image4.png';
import logo from '../../images/logo.svg';

function HomeDefault() {
  return (
    <HomeDefaultContainer>
      <HomeContainer>
        <div className="left">
          <p className="title">All your streaming services in one app.</p>
          <p className="subtitle">
            Get personal recommendations for movies and TV shows available on
            Netflix, Amazon Prime Video, Hotstar and many more.
          </p>
        </div>
        <div className="right">
          <img className="tv" src={image1} />
        </div>
      </HomeContainer>
      <HomeContainer>
        <div className="left">
          <img src={image2} />
        </div>
        <div className="right">
          <p className="pretitle"> ALL IN ONE PLACE</p>
          <p className="title2">Your streaming guide</p>
          <p className="subtitle">
            Get personal recommendations and see what’s new across your favorite
            streaming services.
          </p>
        </div>
      </HomeContainer>
      <HomeContainer>
        <div className="left">
          <p className="pretitle"> ONE SEARCH </p>
          <p className="title2">One search to rule them all</p>
          <p className="subtitle">
            Never go back and forth between your services again to find out if a
            movie or TV show is available.
          </p>
        </div>
        <div className="right">
          <img src={image3} />
        </div>
      </HomeContainer>
      <HomeContainer>
        <div className="left">
          <img src={image4} />
        </div>
        <div className="right">
          <p className="pretitle"> ONE WATCHLIST </p>
          <p className="title2">One search to rule them all</p>
          <p className="subtitle">
            Keep track of all the TV shows and movies you want to watch in one
            list across all your devices
          </p>
        </div>
      </HomeContainer>
      <HomeContainer>
        <div className="container2">
          <img className="logo" src={logo} />
          <p className="title3">
            Get recommendations from all your favorite streaming services in one
            place
          </p>
          <p className="subtitle">Get started by choosing which one you like better:</p>
        </div>
      </HomeContainer>
    </HomeDefaultContainer>
  );
}
export default HomeDefault;

