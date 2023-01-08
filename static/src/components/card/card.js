/** @odoo-module */

import {Component} from "@odoo/owl";

export class Card extends Component {}

Card.template = "booking_management.card";
Card.props = {
  slots: {
    type: Object,
    shape: {
      default: Object,
      title: {type: Object, optional: true},
    },
  },
};
