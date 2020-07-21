import React from 'react';

import styled from 'styled-components';

function Home() {
  return (
    <HomeContainer>
        This is the Home page
    </HomeContainer>
  );
}
export default Home;

const HomeContainer = styled.div`

    display: flex;
    flex-direction: column;
    justify-content:center;
    align-content: center;
    text-align:center;
`;