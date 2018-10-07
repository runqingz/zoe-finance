import React, { Component } from 'react';

import {BootstrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import '../../node_modules/react-bootstrap-table/dist/react-bootstrap-table-all.min.css';

const budgetTypes = [ 'FO', 'CL', 'EL', 'GR', 'TR', 'HR', 'ED', 'ET', 'OT' ];

function isValidDate(value, row)
{
  // First check for the pattern
  if(!/^\d{4}-\d{1,2}-\d{1,2}$/.test(value))
    return false;
  // Parse the date parts to integers
  var parts = value.split("-");
  var day = parseInt(parts[2], 10);
  var month = parseInt(parts[1], 10);
  var year = parseInt(parts[0], 10);
  // Check the ranges of month and year
  if(year < 1000 || year > 3000 || month === 0 || month > 12)
    return false;
  var monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ];
   // Adjust for leap years
  if(year % 400 === 0 || (year % 100 !== 0 && year % 4 === 0))
    monthLength[1] = 29;
  // Check the range of the day
  return day > 0 && day <= monthLength[month - 1];
};

export default class BudgetTable extends Component {

  render() {
    return (
      <BootstrapTable data={ this.props.data }
                      remote={ true }
                      insertRow={ true }
                      options={ { onAddRow: this.props.onAddRow } }>
        <TableHeaderColumn isKey dataField='id' hidden={true} autoValue={ true }>ID</TableHeaderColumn>
        <TableHeaderColumn width='200' dataField='description' editable={ { type: 'textarea' } }>Brief</TableHeaderColumn>
        <TableHeaderColumn width='100' dataField='amount'>Amount</TableHeaderColumn>
        <TableHeaderColumn width='150' dataField='category' editable={ { type: 'select', options: { values: budgetTypes } } }>Category</TableHeaderColumn>
        <TableHeaderColumn width='200' dataField='date' editable={ { validator: isValidDate } }>Date</TableHeaderColumn>
      </BootstrapTable>
    );
  }
}
