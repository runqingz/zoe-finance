import { RSAA } from 'redux-api-middleware';
import { withAuth } from '../reducers'

export const LIST_REQUEST = '@@budgetList/LIST_REQUEST';
export const LIST_SUCCESS = '@@budgetList/LIST_SUCCESS';
export const LIST_FAILURE = '@@budgetList/LIST_FAILURE';

export const getMonthlyList = (year, month) => ({
  [RSAA]: {
      endpoint: `budgets/api/monthly?year=${year}&month=${month}`,
      method: 'GET',
      headers: withAuth({ 'Content-Type': 'application/json' }),
      types: [
        LIST_REQUEST, LIST_SUCCESS, LIST_FAILURE
      ]
  }
})
