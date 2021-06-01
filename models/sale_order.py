from odoo import api, fields, models, _


class sale_order_tax_reductions(models.Model):
    _inherit = "sale.order"

    tax_reductions = fields.One2many('tax_reductions.tax_reduction_line', 'order_id', string="Tax reductions",
                                      states={'cancel': [('readonly', True)], 'done': [('readonly', True)]},
                                      copy=True, auto_join=True)

    def _prepare_invoice_line(self):
        data= super(sale_order_tax_reductions, self)._prepare_invoice_line()
        data['tax_reduction_id'] =  self.tax_reduction_id.id
        return data


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

class OrderLine(models.Model):
    _inherit='sale.order.line'

    tax_reduction_id=fields.Many2one('tax_reductions.tax_reduction','Agevolazioni Fis.')#,domain=[('order_id','=',order_id.id)])

    @api.onchange('order_id.tax_reductions','product_id','name')
    def tax_reduction_id_change(self):
        val = []
        if not self.order_id.tax_reductions:
            return {'domain': {'tax_reduction_id': [('id', '=', val)]}}
        else:
            for res in self.order_id.tax_reductions:
                if res.tax_reduction_id:
                    val.append(res.tax_reduction_id.id)
            return {'domain': {'tax_reduction_id': [('id', '=', val)]}}
class AccountInvoiceLine(models.Model):
    _inherit='account.invoice.line'

    tax_reduction_id=fields.Many2one('tax_reductions.tax_reduction','Agevolazioni Fis.')

    @api.onchange('order_id.tax_reductions', 'product_id', 'name')
    def tax_reduction_id_change(self):
        val = []
        if not self.invoice_id.tax_reductions:
            return {'domain': {'tax_reduction_id': [('id', '=', val)]}}
        else:
            for res in self.invoice_id.tax_reductions:
                if res.tax_reduction_id:
                    val.append(res.tax_reduction_id.id)
            return {'domain': {'tax_reduction_id': [('id', '=', val)]}}
    # @api.onchange('invoice_id')
    # def model_id_change(self):
    #     if not self.order_id:
    #         return {'domain': {'tax_reduction_id': []}}
    #     else:
    #         return {'domain': {'tax_reduction_id': [('move_id', '=', self.invoice_id.id)]}}