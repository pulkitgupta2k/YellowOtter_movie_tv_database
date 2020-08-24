import React from "react";
import Trending from "./Trending";
import GenreList from "./GenreList";
import TopRated from "./TopRated";
import { Flex } from "../../styles/globalStyles";

function HomeWrapper() {
  return (
    <Flex vertical style={{ width: "100vw" }}>
      <TopRated />
      <Trending />
      <GenreList />
    </Flex>
  );
}

export default HomeWrapper;
