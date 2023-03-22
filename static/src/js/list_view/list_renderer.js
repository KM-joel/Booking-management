/** @odoo-module **/
import {Component} from "@odoo/owl";
import {ListItem} from "../components/list_item/list_item";

export class ListRenderer extends Component {
  setup() {
    super.setup();
  }
}

ListRenderer.components = {ListItem};
ListRenderer.template = "booking_management.ListRenderer";
