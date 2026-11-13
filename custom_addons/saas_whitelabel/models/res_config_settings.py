# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    saas_app_name = fields.Char(
        string="SaaS Brand Name",
        config_parameter="saas_whitelabel.app_name",
        default="ConneuralERP",
        help="The brand name displayed in window titles, login page, and user interfaces.",
    )
    saas_company_url = fields.Char(
        string="SaaS Website URL",
        config_parameter="saas_whitelabel.company_url",
        default="https://conneural.com",
        help="Your main platform or company website URL.",
    )
    saas_support_url = fields.Char(
        string="SaaS Support & Helpdesk URL",
        config_parameter="saas_whitelabel.support_url",
        default="https://conneural.com/support",
        help="Support and ticketing URL for your SaaS clients.",
    )
    saas_documentation_url = fields.Char(
        string="SaaS Knowledge Base URL",
        config_parameter="saas_whitelabel.documentation_url",
        default="https://conneural.com/docs",
        help="Documentation or user guide URL for your platform.",
    )
