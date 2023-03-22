/** @odoo-module **/

const {Component, useState} = owl;

import {Todo} from "../todo/todo";
import {useAutofocus} from "../../utils";

export class TodoList extends Component {
  setup() {
    this.nextId = 0;
    this.todoList = useState([]);
    useAutofocus("todoListInput");
  }
  addTodo(ev) {
    if (ev.key === "Enter" && ev.target.value != "") {
      this.todoList.push({
        id: this.nextId++,
        description: ev.target.value,
        done: false,
      });
      ev.target.value = "";
    }
  }
  toggleTodo(todoId) {
    const todo = this.todoList.find((todo) => todo.id === todoId);
    if (todo) {
      todo.done = !todo.done;
    }
  }
  removeTodo(todoId) {
    const todoIndex = this.todoList.findIndex((todo) => todo.id == todoId);
    if (todoIndex >= 0) {
      this.todoList.splice(todoIndex, 1);
    }
  }
}

TodoList.components = {Todo};
TodoList.template = "booking_management.TodoList";
