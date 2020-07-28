
import styled from 'styled-components';
import { generateMedia } from 'styled-media-query';


const customMedia = generateMedia({
    tablet: '740px'
  })
  export const HomeDefaultContainer = styled.div`
    // display:flex;
    display: flex;
    flex-direction:column;
    justify-content: space-between;
    .movie-card {
      border-radius: 12px;
    }
  `;

export const SliderContainer = styled.div`
  margin: 1rem 4rem 0 4rem;
  .title {
    font-size: xxx-large;
    font-weight: bold;
    margin: 1rem auto;
    align-self:center;
  }
  .subtitle {
    margin: 1rem auto;
    // margin-left: 1rem;
    font-size: xx-large;
    align-self:center;
    // font-weight:bold;
  }

  .slider-image-container {
    width: 12%;
    height: 240px;
    margin: 0 0.5em;
    ${customMedia.lessThan('tablet')`
      width:50%;
    `}
  }
  ${customMedia.lessThan('tablet')`
      width:100%;
    `}
`;
export const HeaderHome = styled.div`
  width:80vw;
  height:20vh;
  border-radius:24px;
  margin: 1rem 4rem 1rem 4rem;
  border-radius:24px;
  display:flex-row;
  .header-image{
    width:50vw;
    float:left;
    ${customMedia.lessThan('tablet')`
      width:100%;
    `}
  }
  img{
    width:100%;
    border-top-left-radius:24px;
    border-bottom-left-radius:24px;
    ${customMedia.lessThan('tablet')`
      width:100%;
      border-radius:12px;
      margin-bottom:1rem;
    `}
  }
  .header-title{
    // width:50%;
    // float:right;
  }
  .pretitle{
    font-size:large;
    color:var(--main-yellow);
    ${customMedia.lessThan('tablet')`
      font-size:x-large;
    `}
  }
  .title{
    font-size:xx-large;
    color:var(--main-white);
  }
  ${customMedia.lessThan('tablet')`
      flex-direction:column;
      width:100%;
    `}
`;