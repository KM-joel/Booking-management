/** @odoo-module **/

import {Component, useState} from "@odoo/owl";

export class ListItem extends Component {
  setup() {
    this.state = useState({
      isDraggedOn: false,
    });
  }
}

ListItem.Component = {ListItem};
ListItem.template = "booking_management.ListItem";
