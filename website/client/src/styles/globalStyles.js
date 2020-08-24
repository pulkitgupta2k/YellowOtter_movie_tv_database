import styled, { css } from "styled-components";

export const TitleHeading = styled.h1`
  font-size: 24px;
`;

export const Flex = styled.div`
  position: relative;
  display: flex;
  width:100%;
  align-items: center;
  ${(props) =>
    props.spaceBetween &&
    css`
      justify-content: space-between;
    `}

    ${(props) =>
      props.responsive &&
      css`
        @media (max-width: 1000px) {
          flex-direction: column;
          width: 95%;
        }
      `}

  ${(props) =>
    props.spaceAround &&
    css`
      justify-content: space-around;
    `}
    
	${(props) =>
    props.center &&
    css`
      justify-content: center;
    `}

	${(props) =>
    props.flexEnd &&
    css`
      justify-content: flex-end;
    `}
	${(props) =>
    props.flexStart &&
    css`
      justify-content: flex-start;
    `}
	${(props) =>
    props.alignTop &&
    css`
      align-items: flex-start;
    `}
	${(props) =>
    props.noHeight &&
    css`
      height: 0;
    `}
	${(props) =>
    props.wrap &&
    css`
      flex-wrap: wrap;
    `}

    ${(props) =>
      props.vertical &&
      css`
        flex-direction: column;
      `}
	
	@media(max-width: 700px) {
		flex-direction: column;
		justify-content: center;
	}
`;
