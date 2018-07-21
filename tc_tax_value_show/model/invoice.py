# -*- coding:utf-8 -*-

from odoo import models, fields, api, _


class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'
    
    @api.one
    @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
        'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id',
        'invoice_id.date_invoice', 'invoice_id.date')
    def _compute_price(self):
        res = super(AccountInvoiceLine, self)._compute_price()
        currency = self.invoice_id and self.invoice_id.currency_id or None
        price = self.price_unit * (1 - (self.discount or 0.0) / 100.0)
        taxes = False
        if self.invoice_line_tax_ids:
            taxes = self.invoice_line_tax_ids.compute_all(price, currency, self.quantity, product=self.product_id, partner=self.invoice_id.partner_id)
        if taxes:
            self.price_tax = taxes['total_included'] - taxes['total_excluded']
            self.total_with_tax = taxes['total_included']

    price_tax = fields.Float(string='Taxes Amount', compute='_compute_price', help="Taxes amount")
    total_with_tax = fields.Float(string='Total with Taxes', compute='_compute_price', help="Total With Taxes")
    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
