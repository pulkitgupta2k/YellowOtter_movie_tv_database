/** @format */

import {
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT_USER,
  SET_LOADING,
  RESET_STATE,
} from "../actions";

const defaultState = {
  token: null,
  isAuthenticated: false,
  loading: false,
  user: null,
  error: null,
};

export default (state = defaultState, action) => {
  switch (action.type) {
    case LOGIN_SUCCESS:
      return {
        ...state,
        token: action.payload.access_token,
        user: action.payload.username,
        isAuthenticated: true,
        loading: false,
        error: null,
      };
    case LOGIN_FAIL:
    case LOGOUT_USER:
      return {
        ...state,
        token: null,
        isAuthenticated: false,
        loading: false,
        user: null,
        error: action.payload,
      };
    case SET_LOADING:
      return {
        ...state,
        loading: true,
      };
    case RESET_STATE:
      return defaultState;
    default:
      return state;
  }
};
