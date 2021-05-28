from odoo import api, fields, models, _


class tax_reduction(models.Model):
    _name = 'tax_reductions.tax_reduction'
    _description = 'Tax reduction'

    name = fields.Char(string='Name')
    document_text = fields.Char(string='Document text')


class tax_reduction_line(models.Model):
    _name = 'tax_reductions.tax_reduction_line'
    _description = 'Tax reduction line'

    tax_reduction_id = fields.Many2one('tax_reductions.tax_reduction', string='Tax reduction')
    amount = fields.Float('Amount', digits=(12, 4))

    order_id = fields.Many2one('sale.order', string='Order reference', ondelete='cascade', copy=False)
    move_id = fields.Many2one('account.invoice', string='Invoice reference', ondelete='cascade', copy=False)
