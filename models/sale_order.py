from odoo import api, fields, models, _


class sale_order_tax_reductions(models.Model):
    _inherit = "sale.order"

    tax_reductions = fields.One2many('tax_reductions.tax_reduction_line', 'order_id', string="Tax reductions",
                                      states={'cancel': [('readonly', True)], 'done': [('readonly', True)]},
                                      copy=True, auto_join=True)

    def _prepare_invoice(self):
        """Copies the tax reductions values into the invoice"""
        res = super(sale_order_tax_reductions, self)._prepare_invoice()

        tax_reductions_list = [(5, 0, 0), ]
        # For each tax_reduction create the tax_reduction_line
        for tac_red in self.tax_reductions:
            tr = (0, 0, {'tax_reduction_id': tac_red.tax_reduction_id.id, 'amount': tac_red.amount})
            tax_reductions_list.append(tr)

        # Adding the tax_reductions_line to the res values
        res['tax_reductions'] = tax_reductions_list

        return res
