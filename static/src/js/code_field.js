/** @odoo-module **/

const {xml, Component} = owl;
import {standardFieldProps} from "@web/views/fields/standard_field_props";
import {registry} from "@web/core/registry";

export class CodeField extends Component {
  setup() {
    super.setup();
  }
}

CodeField.template = xml`<pre t-esc="props.value" rows="5" t-attf-class="bg-#{props.backgroundColor} text-white p-3 rounded"/>`;
CodeField.defaultProps = {backgroundColor: "primary"};
CodeField.props = {
  ...standardFieldProps,
  backgroundColor: {type: String, optional: true},
};
// ({attrs, field})
CodeField.extractProps = ({attrs}) => {
  return {
    backgroundColor: attrs.background_color,
  };
};

registry.category("fields").add("code", CodeField);
