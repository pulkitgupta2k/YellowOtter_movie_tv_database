import Flickity from "react-flickity-component";
import React from "react";
import "./flickity.css";
const flickityOptions = {
  initialIndex: 0,
  draggable: true,
  contain: true,
  pageDots: false,
  freeScroll: true,
  prevNextButtons: true,
  cellAlign: "left",
  bgLazyLoad: 1,
};
function FlickityWrapper(props) {
  return (
    <Flickity
      className={"carousel"} // default ''
      elementType={"div"} // default 'div'
      options={flickityOptions} // takes flickity options {}
      disableImagesLoaded={false} // default false
      reloadOnUpdate // default false
      static // default false
    >
      {[1, 2, 3, 4, 5].map((e) => {
        return <div style={{ height: "20vh", width: "30vw" }}>Hello {e}</div>;
      })}
    </Flickity>
  );
}

export default FlickityWrapper;
