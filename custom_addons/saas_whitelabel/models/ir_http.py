# -*- coding: utf-8 -*-
from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super().session_info()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        brand_name = get_param('saas_whitelabel.app_name', 'CloudERP')
        result['saas_brand_name'] = brand_name
        result['saas_company_url'] = get_param('saas_whitelabel.company_url', 'https://yourcompany.com')
        result['saas_support_url'] = get_param('saas_whitelabel.support_url', 'https://yourcompany.com/support')
        result['saas_documentation_url'] = get_param('saas_whitelabel.documentation_url', 'https://yourcompany.com/docs')
        return result

    def get_frontend_session_info(self):
        result = super().get_frontend_session_info()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        result['saas_brand_name'] = get_param('saas_whitelabel.app_name', 'CloudERP')
        result['saas_company_url'] = get_param('saas_whitelabel.company_url', 'https://yourcompany.com')
        return result

