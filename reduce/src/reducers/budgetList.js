import * as budgetList from '../actions/budgetList'

const initialState = {
  data: []
}

export default (state=initialState, action) => {
  switch(action.type) {
    case budgetList.LIST_SUCCESS:
      return {
        data: action.payload
      }
    default:
      return state
  }
}

export const monthlyList = (state) => state.data
