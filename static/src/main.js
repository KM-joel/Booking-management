/** @odoo-module **/

// import {browser} from "@web/core/browser/browser";
import {mount} from "@odoo/owl";
import {Playground} from "./js/playground";

import {templates} from "@web/core/assets";

owl.whenReady(() => {
  mount(Playground, document.body, {templates, dev: true});
});
