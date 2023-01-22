/** @odoo-module */

import {Component, useState} from "@odoo/owl";

export class Counter extends Component {
  setup() {
    this.state = useState({val: 1});
  }

  increment() {
    this.state.val++;
  }
}
Counter.template = "booking_management.counter";
