# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    check_sale = fields.Boolean("Procurements")

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        params = self.env['ir.config_parameter'].sudo()

        # Check if the module was disabled in the inventory settings
        if bool(params.get_param('procurement_paid.check_sale', default=False)) is True and self.check_sale is False:
            params.set_param("procurement_paid.check_sale", self.check_sale)

            # Create procurements for sales that don't have after the module has been disabled
            for sale in self.env['sale.order'].sudo().search([]):
                if sale.delivery_count == 0 and sale.invoice_count > 0:
                    for line in sale.order_line:
                        print("LAUNCH")
                        print(sale.name)
                        line.sudo()._action_launch_procurement_rule()
        else:
            params.set_param("procurement_paid.check_sale", self.check_sale)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res['check_sale'] = params.get_param('procurement_paid.check_sale', default=False)
        return res
