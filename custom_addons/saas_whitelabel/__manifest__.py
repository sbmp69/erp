# -*- coding: utf-8 -*-
{
    'name': 'SaaS White-Label Suite',
    'version': '18.0.1.0.0',
    'summary': 'Full White-Labeling, Custom Branding and Multi-Tenant SaaS Engine',
    'description': """
SaaS White-Label Suite for Odoo 18
==================================
* Complete white-labeling: dynamic brand name in page title, footer, and emails.
* Removes/replaces Odoo links with your SaaS company domain.
* Customizable SaaS documentation & support URLs in the user dropdown.
* Configurable directly from Settings -> General Settings -> SaaS White-Label.
* Blocks external Odoo Enterprise industry templates and sales upsells.
* Filters out third-party Chrome extension errors (MetaMask, etc.).
* Ready for multi-tenant database routing and sub-domain isolation.
    """,
    'category': 'Administration',
    'author': 'Your SaaS Team',
    'website': 'https://yourcompany.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'portal',
        'base_setup',
        'base_import_module',
    ],
    'data': [
        'data/ir_config_parameter_data.xml',
        'views/web_login_templates.xml',
        'views/res_config_settings_views.xml',
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
