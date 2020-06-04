odoo.define('raumschmiede.relational_fields', function (require) {
"use strict";

var relational_fields = require('web.relational_fields');
var registry = require('web.field_registry');


var FieldMany2ManyCheckBoxesEdit = relational_fields.FieldMany2ManyCheckBoxes.extend({
    _renderReadonly: function () {
        this._renderCheckboxes();
    },
});

registry.add('many2many_checkboxes_edit', FieldMany2ManyCheckBoxesEdit);
})
