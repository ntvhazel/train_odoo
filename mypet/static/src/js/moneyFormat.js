odoo.define('mypet.moneyFormat', function (require){
    "use strict";
    // import packages
    var basic_fields = require('web.basic_fields');
    var registry = require('web.field_registry');

    // widget implementation
    var moneyWidget = basic_fields.FieldChar.extend({
        _renderReadonly: function () {
            this._super();
            var old_html_render = this.$el.html();
            var clean_format = old_html_render.replace(/,/g, '')
            var reformat = parseFloat(clean_format)
            var final_format = reformat.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' });
            console.log(final_format);
            this.$el.html(final_format)
        }
    })
    registry.add('format_money', moneyWidget); // add our "bold" widget to the widget registry
})