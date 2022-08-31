odoo.define("Booking-management.booking_management_reservation", function (require){
    "use strict";

    const core = require('web.core');
    const _t = core._t;

    var FormController = require('web.FormController');

    var ExtendFormController = FormController.include({
        saveRecord: function () {
            // console.log('Save record')
            var res = this._super.apply(this, arguments);
            if (this.modelName === 'booking.management.reservation'){
                // this.displayNotification({title: _t('Success'), message: _t('Record saved'), type: 'success'});
                self = this
                self._rpc({
                    model: 'booking.management.reservation',
                    method: 'search_read',
                    fields: ['reference', 'client_id', 'state', 'total_duration_hours'],
                    context: self.context,
                }).then( function (result) {
                    console.log(result)
                    if (result[0]['total_duration_hours'] == 0){
                        self.displayNotification({title: _t('Warning'), message: _t('Total hours is 0'), type: 'warning'});
                    }
                })
            }
            return res;
        }
    });
});