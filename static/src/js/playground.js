/** @odoo-module **/

import {Card} from "../components/card/card";
import {Component} from "@odoo/owl";
import {Counter} from "../components/counter/counter";
import {TodoList} from "../components/todo_list/todo_list";

export class Playground extends Component {}
Playground.template = "booking_management.playground";
Playground.components = {Card, Counter, TodoList};
