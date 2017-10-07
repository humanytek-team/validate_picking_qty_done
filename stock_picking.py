# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError


class stock_picking(models.Model):
	_inherit = ['stock.picking']


	@api.multi
	def do_new_transfer(self):
		if (self.picking_type_id.code == 'outgoing' or self.picking_type_id.code == 'internal') and self.pack_operation_ids:
			for operation in self.pack_operation_ids:
				if operation.qty_done > operation.product_qty:
					raise ValidationError(_('No se pueda entregar más de lo que está establecido.'))

		return super(stock_picking,self).do_new_transfer()