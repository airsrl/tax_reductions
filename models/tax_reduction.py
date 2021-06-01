from odoo import api, fields, models, _
from odoo.addons.l10n_it_fatturapa.bindings.fatturapa import (
    FatturaElettronica,
    FatturaElettronicaHeaderType,
    DatiTrasmissioneType,
    IdFiscaleType,
    ContattiTrasmittenteType,
    CedentePrestatoreType,
    AnagraficaType,
    IndirizzoType,
    IscrizioneREAType,
    CessionarioCommittenteType,
    RappresentanteFiscaleType,
    DatiAnagraficiCedenteType,
    DatiAnagraficiCessionarioType,
    DatiAnagraficiRappresentanteType,
    TerzoIntermediarioSoggettoEmittenteType,
    DatiAnagraficiTerzoIntermediarioType,
    FatturaElettronicaBodyType,
    DatiGeneraliType,
    DettaglioLineeType,
    DatiBeniServiziType,
    DatiRiepilogoType,
    DatiGeneraliDocumentoType,
    DatiDocumentiCorrelatiType,
    ContattiType,
    DatiPagamentoType,
    DettaglioPagamentoType,
    AllegatiType,
    ScontoMaggiorazioneType,
    CodiceArticoloType,
    AltriDatiGestionaliType
)

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

class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"

    def setDatiGeneraliDocumento(self, invoice, body):
        res =super(WizardExportFatturapa, self).setDatiGeneraliDocumento(invoice,body)
        if invoice.tax_reductions:
            for reduction in invoice.tax_reductions:
                body.DatiGenerali.DatiGeneraliDocumento.ScontoMaggiorazione.append(ScontoMaggiorazioneType(
                        Tipo='SC',
                        Importo=reduction.amount
                    ))
        return res

    def setRiferimentoTesto(self, line):
        res = []
        if line.tax_reduction_id:
            if line.tax_reduction_id.document_text:
                res.append(AltriDatiGestionaliType(
                    RiferimentoTesto='esempio'
                ))

        return res
    #todo da completare
    # def setDettaglioLinea( self, line_no, line, body, price_precision, uom_precision ):
    #     DettaglioLinea = super(WizardExportFatturapa, self).setDettaglioLinea(
    #         line_no, line, body, price_precision, uom_precision)
    #     if line.tax_reduction_id:
    #         if line.tax_reduction_id.document_text:
    #             dati_gestionali = AltriDatiGestionaliType()
    #             dati_gestionali.RiferimentoTesto = str(line.tax_reduction_id.document_text)
    #             DettaglioLinea.AltriDatiGestionali.append(
    #                 dati_gestionali
    #             )

        # return DettaglioLinea
