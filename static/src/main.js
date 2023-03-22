/** @odoo-module **/

// import {browser} from "@web/core/browser/browser";
const {mount} = owl;
import {Playground} from "./js/playground";
import {templates} from "@web/core/assets";

owl.whenReady(() => {
  mount(Playground, document.body, {templates, dev: true});
});
