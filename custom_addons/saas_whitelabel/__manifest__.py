# -*- coding: utf-8 -*-
{
    'name': 'ConneuralERP White-Label & SaaS Suite',
    'version': '18.0.1.0.0',
    'summary': 'Full A-to-Z White-Labeling, Custom Branding and Multi-Tenant SaaS Engine for ConneuralERP',
    'description': """
ConneuralERP White-Label Suite for Odoo 18
==========================================
* Complete white-labeling: ConneuralERP brand name across page titles, footers, database managers, and email templates.
* Replaces all Odoo links with ConneuralERP platform endpoints.
* Custom ConneuralERP documentation & support URLs in the user menu.
* Configurable from Settings -> General Settings -> SaaS White-Labeling & Branding.
* Blocks external Odoo Enterprise industry templates and sales upsells.
* Filters out third-party Chrome extension errors (MetaMask, etc.).
* Ready for multi-tenant database routing and sub-domain isolation.
    """,
    'category': 'Administration',
    'author': 'Conneural Technologies',
    'website': 'https://conneural.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'portal',
        'mail',
        'base_setup',
        'base_import_module',
    ],
    'data': [
        'data/ir_config_parameter_data.xml',
        'views/web_login_templates.xml',
        'views/res_config_settings_views.xml',
        'views/mail_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'saas_whitelabel/static/src/scss/whitelabel.scss',
            'saas_whitelabel/static/src/js/extension_error_filter.js',
            'saas_whitelabel/static/src/js/title_service_patch.js',
            'saas_whitelabel/static/src/js/user_menu_patch.js',
        ],
        'web.assets_frontend': [
            'saas_whitelabel/static/src/scss/frontend_whitelabel.scss',
            'saas_whitelabel/static/src/js/extension_error_filter.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
