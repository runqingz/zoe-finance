import { RSAA } from 'redux-api-middleware';
import { withAuth } from '../reducers'

export const SUM_REQUEST = '@@budgetStats/SUM_REQUEST';
export const SUM_SUCCESS = '@@budgetStats/SUM_SUCCESS';
export const SUM_FAILURE = '@@budgetStats/SUM_FAILURE';

export const getMonthlySum = (year, month) => ({
  [RSAA]: {
      endpoint: `budgets/api/monthly_sum?year=${year}&month=${month}`,
      method: 'GET',
      headers: withAuth({ 'Content-Type': 'application/json' }),
      types: [
        SUM_REQUEST, SUM_SUCCESS, SUM_FAILURE
      ]
  }
})
