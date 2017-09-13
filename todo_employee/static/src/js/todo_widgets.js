odoo.define('web.form_widgets', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    // var crash_manager = require('web.crash_manager');
    // var data = require('web.data');
    // var datepicker = require('web.datepicker');
    // var dom_utils = require('web.dom_utils');
    // var Priority = require('web.Priority');
    // var ProgressBar = require('web.ProgressBar');
    // var Dialog = require('web.Dialog');
    var common = require('web.form_common');
    // var formats = require('web.formats');
    // var framework = require('web.framework');
    // var Model = require('web.DataModel');
    // var pyeval = require('web.pyeval');
    // var session = require('web.session');
    // var utils = require('web.utils');

    var _t = core._t;
    var QWeb = core.qweb;

    var LeavesButton = common.AbstractField.extend({
    className: 'o_stat_info',
    init: function() {
        this._super.apply(this, arguments);
        switch (this.options["terminology"]) {
            case "leaves":
                this.string_true = _t("正在离职中...");
                this.hover_true = _t("完全离职");
                this.string_false = _t("完全离职");
                this.hover_false = _t("取消完全离职");
                break;

            default:
                var terms = typeof this.options["terminology"] === 'string' ? {} : this.options["terminology"];
                this.string_true = _t(terms.string_true || "On");
                this.hover_true = _t(terms.hover_true || terms.string_false || "Switch Off");
                this.string_false = _t(terms.string_false || "Off");
                this.hover_false = _t(terms.hover_false || terms.string_true || "Switch On");
        }
    },
    render_value: function() {
        this._super();
        this.$el.html(QWeb.render("BooleanButton", {widget: this}));
    },
    is_false: function() {
        return false;
    },
});


core.form_widget_registry.add('leaves_button', LeavesButton)

});