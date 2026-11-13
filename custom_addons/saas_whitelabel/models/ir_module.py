# -*- coding: utf-8 -*-
from odoo import api, models


class IrModule(models.Model):
    _inherit = 'ir.module.module'

    @api.model
    def _call_apps(self, payload):
        """
        Block remote Odoo Enterprise industry templates and external upsells.
        Forces the Apps view to show only real, working open-source Community applications.
        """
        class DummyResponse:
            def raise_for_status(self):
                pass

            def json(self):
                return {'result': []}

        return DummyResponse()

    @api.model
    def _get_industry_categories_from_apps(self):
        """Disable remote industry categories that require Enterprise."""
        return []

