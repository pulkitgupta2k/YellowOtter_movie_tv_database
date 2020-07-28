import React from 'react';

import styled from 'styled-components';

//Components
import HomeDefault from '../components/Home/index';
import HomeAuthenticated from '../components/HomeAuthenticated/index';

function Home() {
  return (
    <div>
      {/* <HomeDefault /> */}
      <HomeAuthenticated />
    </div>
  );
}
export default Home;
