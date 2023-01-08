/** @odoo-module **/

import {Card} from "../components/card/card";
import {Counter} from "../components/counter/counter";
import {Component} from "@odoo/owl";

export class Playground extends Component {
  static template = "booking_management.playground";
  static components = {Card, Counter};
}
