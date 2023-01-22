/** @odoo-module **/

import {useAutofocus} from "../../utils";

import {Component, useState} from "@odoo/owl";

export class TodoList extends Component {
  setup() {
    this.nextId = 0;
    this.todoList = useState([]);
    useAutofocus("todoListInput");
  }
  addTodo(ev) {
    if (ev.target.value != "") {
      this.todoList.push({
        id: this.nextId++,
        description: ev.target.value,
        done: false,
      });
      ev.target.value = "";

      console.log("+++++++++++++++++++++++", useAutofocus);
      console.log("+++++++++++++++++++++++", ev.target.value);
    }
  }
}

TodoList.template = "booking_management.TodoList";
