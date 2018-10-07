import React, { Component } from 'react';
import './App.css';
import { connect } from 'react-redux'

import {getMonthlySum} from './actions/budgetStats'
import {monthlySum} from './reducers/budgetStats'

import {getMonthlyList} from './actions/budgetList'
import {monthlyList} from './reducers/budgetList'

import BudgetTable from './components/budgetTable'

class App extends Component {
  componentDidMount() {
      this.props.fetchSum(2018, 8)
      this.props.fetchList(2018, 8)
  }

  onAddRow(row) {
    alert("insert row")
  }

  render() {
    return (
      <div className = "main-body">
        <div className="stats">
          <h2>
            Current Expense:{this.props.sum.sum}
          </h2>
        </div>
        <div className="budget-table">
	    < BudgetTable onAddRow={ this.onAddRow.bind(this) } { ...this.props.data } />
        </div>
      </div>
    );
  }
}

export default connect(
  state => ({ sum: monthlySum(state), data: monthlyList(state) }),
  { fetchSum: getMonthlySum, fetchList: getMonthlyList }
)(App);

//export default App;
