// /** @odoo-module **/
//
// import {registry} from "@web/core/registry";
// import {Layout} from "@web/search/layout";
// import {KeepLast} from "@web/core/utils/concurrency";
// import {Model, useModel} from "@web/views/model";
// import {standardViewProps} from "@web/views/standard_view_props";
//
// const {xml, Component} = owl;
//
// class VeryBasicModel extends Model {
//  static services = ["orm"];
//
//  setup(params, {orm}) {
//    this.model = params.resModel;
//    this.orm = orm;
//    this.KeepLast = new keepLast();
//  }
//
//  async load(params) {
//    this.data = await this.keepLast.add(
//      this.orm.searchRead(this.model, params.domain, [], {limit: 100})
//    );
//    this.notify();
//  }
// }
// VeryBasicModel.services = ["orm"];
//
// export class VeryBasicView extends Component {
//  setup() {
//    this.model = useModel(VeryBasicModel, {
//      resModel: this.props.resModel,
//      domain: this.props.domain,
//    });
//    onWillStart(async () => {
//      this.data = await this.loadData();
//    });
//  }
// }
//
// VeryBasicView.type = "very_basic_view";
// VeryBasicView.display_name = "VeryBasicView";
// VeryBasicView.icon = "fa-indent";
// VeryBasicView.multiRecord = true;
// VeryBasicView.searchMenuTypes = ["filter", "favorite"];
// VeryBasicView.components = {Layout};
// VeryBasicView.props = {
//  ...standardViewProps,
// };
//
// VeryBasicView.template = xml`
// <Layout viewType="'very_basic_view'">
//    <div><h1>Hello OwlView</h1></div>
//    <div t-foreach="model.data" t-as="record" t-key="record.id">
//        <t t-esc="record.name"/>
//    </div>
// </Layout>`;
//
// console.log("++++++++++++++++++++++++++++++++++++", VeryBasicView);
// registry.category("views").add("very_basic_view", VeryBasicView);
