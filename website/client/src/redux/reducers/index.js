/** @format */

import { combineReducers } from "redux";
import genReducer from "./genReducer";
import authReducer from "./authReducer";
const rootReducer = combineReducers({
  auth: authReducer,
  gen: genReducer,
});

export default rootReducer;
