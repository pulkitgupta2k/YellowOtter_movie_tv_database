import React from 'react';

import styled from 'styled-components';
import { generateMedia } from 'styled-media-query';
import { HomeDefaultContainer, HeaderHome, SliderContainer } from "./styles";

import image1 from '../../images/movie1.jfif';
import image2 from '../../images/movie2.jfif';
import image3 from '../../images/movie3.jfif';
import image4 from '../../images/movie4.jfif';
import image5 from '../../images/movie5.jfif';
import image6 from '../../images/movie6.jfif';
import image7 from '../../images/movie7.jfif';
import image8 from '../../images/movie8.jfif';
import image9 from '../../images/movie9.jfif';
import headerImage from '../../images/home_recommendations.png';
import logo from '../../images/logo.svg';
import Slider from '../Slider';

const images = [image1, image2, image3, image4, image5, image6, image7, image8, image9];

function HomeAuthenticated() {
  return (
    <HomeDefaultContainer>
      <HeaderHome>
        <div className="header-image">
          <img src={headerImage} />
        </div>
        <div className="header-title">
          <p className="pretitle">GET STARTED</p>
          <p className="title">Get recommendations based on your taste</p>
          <button className="header-btn">Start Now</button>
        </div>
      </HeaderHome>
      <SliderContainer>
        <p className="title">Movies that you may like</p>
        <p className="subtitle">Movies that make you feel grateful</p>
        <Slider
          options={{
            autoPlay: 2000,
            pauseAutoPlayOnHover: true,
            wrapAround: true,
            fullscreen: true,
            adaptiveHeight: true,
            prevNextButtons: false,
            pageDots: false,
          }}
        >
          {images.map((image, index) => (
            <div
              className="slider-image-container"
              key={index}
            >
              <img className="movie-card" src={image} alt="" />
            </div>
          ))}
        </Slider>
      </SliderContainer>
      <SliderContainer>
        <p className="subtitle">Because you watched Dark</p>
        <Slider
          options={{
            autoPlay: 1500,
            pauseAutoPlayOnHover: true,
            wrapAround: true,
            fullscreen: true,
            adaptiveHeight: true,
            prevNextButtons: false,
            pageDots: false,
          }}
        >
          {images.map((image, index) => (
            <div
              className="slider-image-container"
              key={index}
            >
              <img className="movie-card" src={image} alt="" />
            </div>
          ))}
        </Slider>
      </SliderContainer>
      <SliderContainer>
        <p className="subtitle">Users with similar tastes watched this</p>
        <Slider
          options={{
            autoPlay: 1500,
            pauseAutoPlayOnHover: true,
            wrapAround: true,
            fullscreen: true,
            adaptiveHeight: true,
            prevNextButtons: false,
            pageDots: false,
          }}
        >
          {images.map((image, index) => (
            <div
              className="slider-image-container"
              key={index}
            >
              <img className="movie-card" src={image} alt="" />
            </div>
          ))}
        </Slider>
      </SliderContainer>
    </HomeDefaultContainer>
  );
}
export default HomeAuthenticated;
