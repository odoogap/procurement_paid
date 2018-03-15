# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def _action_launch_procurement_rule(self):
        for rec in self:
            if self.env['ir.config_parameter'].sudo().get_param('procurement_paid.check_sale', default=False):
                orders = list(set(x.order_id for x in rec))
                for order in orders:
                    invoices = order.invoice_ids

                    if (invoices and all(
                            [x.residual <= 0 and x.state != 'draft' for x in invoices])) or self.env.context.get(
                        'btn_procur') is True:
                        return super(SaleOrderLine, self)._action_launch_procurement_rule()
            else:
                return super(SaleOrderLine, self)._action_launch_procurement_rule()


class account_payment(models.Model):
    _inherit = 'account.payment'

    def action_validate_invoice_payment(self):

        res = super(account_payment, self).action_validate_invoice_payment()

        if self.env['ir.config_parameter'].sudo().get_param('procurement_paid.check_sale', default=False):

            for invoice in self.invoice_ids:
                sale_order = self.env['sale.order'].search([('name', '=', invoice.origin)])

                if not sale_order.picking_ids:
                    for line in sale_order.order_line:
                        line._action_launch_procurement_rule()
        return res


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    btn_procur = fields.Boolean(compute='compute_module_active')

    @api.multi
    def compute_module_active(self):
        IrConfigParameterSudo = self.env['ir.config_parameter'].sudo()
        for rec in self:
            rec.btn_procur = IrConfigParameterSudo.get_param('procurement_paid.check_sale', default=False)

    def action_ignore_payment(self):
        for line in self.order_line:
            line._action_launch_procurement_rule()
