/** @odoo-module **/

import {Card} from "../components/card/card";
import {Counter} from "../components/counter/counter";
import {TodoList} from "../components/todo_list/todo_list";
import {Component} from "@odoo/owl";

export class Playground extends Component {
  static template = "booking_management.playground";
  static components = {Card, Counter, TodoList};
}
