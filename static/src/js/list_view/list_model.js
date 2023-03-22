/** @odoo-module **/
import {KeepLast} from "@web/core/utils/concurrency";

export class ListModel {
  constructor(orm, rpc, resModel, fields, archInfo = false, domain, context) {
    this.orm = orm;
    this.rpc = rpc;
    this.resModel = resModel;
    this.fields = fields;
    this.archInfo = archInfo;
    this.domain = domain;
    this.context = context;
    this.data = [];
    this.keepLast = new KeepLast();
  }

  async load() {
    let result = await this.keepLast.add(
      this.orm.searchRead(this.resModel, domain, [])
    );
    this.data = result;
  }
}
