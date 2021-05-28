from odoo import api, fields, models, _
import xml.etree.ElementTree as etree
import logging

_logger = logging.getLogger(__name__)

class account_move_template(models.Model):
    _inherit = "account.move"

    tax_reductions = fields.One2many('tax_reductions.tax_reduction_line', 'move_id', string="Tax reductions",
                                      states={'posted': [('readonly', True)], 'cancel': [('readonly', True)]},
                                      copy=True, auto_join=True)


class attachment_tax_reductions(models.Model):
    _inherit = "ir.attachment"

    def get_xml_string(self):
        _logger.info("super - get_xml_string")
        try:
            """ Add ScontoMaggiorazione in the xml file """
            res = super(attachment_tax_reductions, self).get_xml_string()
            data = etree.parse(res).getroot()

            logger.info(data)

            # Getting DatiGeneraliDocumento node element
            DatiGeneraliDocumento = data.find('FatturaElettronicaBody/DatiGenerali/DatiGeneraliDocumento')

            # Creating Tipo and Importo nodes
            ScontoMaggiorazione = etree.Element('ScontoMaggiorazione')
            Tipo = etree.Element('Tipo')
            Tipo.text = 'SC'
            ScontoMaggiorazione.append(Tipo)

            Importo = etree.Element('Importo')
            Importo.text = '1936.27'
            ScontoMaggiorazione.append(Importo)
            DatiGeneraliDocumento.append(ScontoMaggiorazione)
        except Exception as e:
            raise e

        return res.cleanup_xml(data)
