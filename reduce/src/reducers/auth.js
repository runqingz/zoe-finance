import jwtDecode from 'jwt-decode'
import * as auth from '../actions/auth'

const initialState = {
  access: undefined,
  errors: {},
}

export default (state=initialState, action) => {
  switch(action.type) {
    case auth.LOGIN_SUCCESS:
      return {
        access: {
          token: action.payload.token,
          ...jwtDecode(action.payload.token, "finance_sercret_key")
        },
        errors: {}
    }
    case auth.LOGIN_FAILURE:
      return {
         access: undefined,
         errors: 
             action.payload.response || 
                {'non_field_errors': action.payload.error},
      }
    default:
      return state
    }
}

export function accessToken(state) {
    if (state.access) {
        return  state.access.token
    }
}
    
export function isAccessTokenExpired(state) {
  if (state.access && state.access.exp) {
    return 1000 * state.access.exp - (new Date()).getTime() < 5000
  }
  return true
}


export function isAuthenticated(state) {
  return !isAccessTokenExpired(state)
}

export function errors(state) {
   return  state.errors
}
