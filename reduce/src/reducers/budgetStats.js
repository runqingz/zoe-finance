import * as budgetStats from '../actions/budgetStats'

const initialState = {
  sum: 0,
}

export default (state=initialState, action) => {
  switch(action.type) {
    case budgetStats.SUM_SUCCESS:
      return {
        sum: action.payload[0].amount_sum
      }
    default:
      return state
  }
}

export const monthlySum = (state) => state.sum
