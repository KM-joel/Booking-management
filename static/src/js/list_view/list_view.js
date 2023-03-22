/** @odoo-module **/
import {_t} from "@web/core/l10n/translation";
import {registry} from "@web/core/registry";

import {ListController} from "./list_controller";
import {ListModel} from "./list_model";
import {ListRenderer} from "./list_renderer";

export const owlListView = {
  type: "owl_list",
  display_name: _t("OWL List"),
  icon: "fa-indent",
  multiRecord: true,
  Controller: ListController,
  Model: ListModel,
  Renderer: ListRenderer,

  props(genericProps, view) {
    const {ArchParser} = view;
    const {arch, relatedModels} = genericProps;
    const archInfo = new ArchParser().parse(arch);
    return {
      ...genericProps,
      Model: view.Model,
      Renderer: view.Renderer,
      archInfo,
    };
  },
};

registry.category("views").add("owl_list", owlListView);
