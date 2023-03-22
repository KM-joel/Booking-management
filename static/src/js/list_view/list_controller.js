/** @odoo-module **/
import {Component, useState, onWillStart, onWillUpdateProps} from "@odoo/owl";
import {Layout} from "@web/search/layout";
import {useService} from "@web/core/utils/hooks";

export class ListController extends Component {
  setup() {
    this.orm = useService("orm");
    this.rpc = useService("rpc");
    this.model = useState(
      new this.props.Model(
        this.orm,
        this.props.resModel,
        this.props.fields,
        this.props.archInfo,
        this.props.domain,
        this.props.context,
        this.rpc
      )
    );

    onWillStart(async () => {
      await this.model.load();
    });
  }
}

ListController.components = {Layout};
ListController.template = "booking_management.View";
