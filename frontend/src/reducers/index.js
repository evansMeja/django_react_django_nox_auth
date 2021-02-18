import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';
import todos from './todos';
import auth from './auth'; // added

import { LOGOUT_SUCCESS } from '../actions/types'; // added

// export default combineReducers({
//   form: formReducer,
//   todos,
//   auth // added
// });

const appReducer = combineReducers({
  form: formReducer,
  todos,
  auth
});

const rootReducer = (state, action) => {
  if (action.type === LOGOUT_SUCCESS) {
    state = undefined;
  }
  return appReducer(state, action);
};

export default rootReducer;