import { combineReducers } from 'redux'
import { routerReducer } from 'react-router-redux'
import auth, * as fromAuth from './auth.js'
import sum, * as fromSum from './budgetStats'
import data, * as fromList from './budgetList'

export default combineReducers({
  auth: auth,
  router: routerReducer,
  sum: sum,
  data: data
})

export const isAuthenticated =
 state => fromAuth.isAuthenticated(state.auth)

export const accessToken =
  state => fromAuth.accessToken(state.auth)

export const isAccessTokenExpired =
  state => fromAuth.isAccessTokenExpired(state.auth)

export const authErrors =
  state => fromAuth.errors(state.auth)

export const fetchSum = state => fromSum(state.sum)

export const fetchList = state => fromList(state.data)

export function withAuth(headers={}) {
  return (state) => ({
    ...headers,
    'Authorization': `JWT ${accessToken(state)}`
  })
}

