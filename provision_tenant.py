#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CloudERP Multi-Tenant SaaS Provisioning Script
==============================================
Quickly provisions isolated tenant databases with automatic white-labeling,
admin user initialization, and pre-selected business modules.

Usage:
    python provision_tenant.py --tenant acme --company "Acme Corp" --admin-email "admin@acme.com" --admin-password "secret123"
"""

import argparse
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")
ODOO_BIN = os.path.join(BASE_DIR, "odoo", "odoo-bin")
ODOO_CONF = os.path.join(BASE_DIR, "odoo.conf")


def parse_args():
    parser = argparse.ArgumentParser(description="Provision a new SaaS tenant database in CloudERP.")
    parser.add_argument("--tenant", required=True, help="Tenant identifier (subdomain/database name), e.g. acme")
    parser.add_argument("--company", required=True, help="Tenant company display name, e.g. 'Acme Corp'")
    parser.add_argument("--admin-email", default="admin@example.com", help="Tenant administrator email")
    parser.add_argument("--admin-password", default="admin", help="Tenant administrator password")
    parser.add_argument("--brand-name", default="CloudERP", help="White-labeled platform name")
    parser.add_argument("--modules", default="crm,sale_management", help="Comma-separated extra modules to install")
    return parser.parse_args()


def provision_tenant(args):
    db_name = args.tenant.lower().replace("-", "_").strip()
    print("=" * 60)
    print(f"Provisioning SaaS Tenant: {args.company} (DB: {db_name})")
    print("=" * 60)

    # Core white-label and security modules
    base_modules = [
        "base",
        "web",
        "portal",
        "base_setup",
        "saas_whitelabel",
        "remove_odoo_enterprise",
        "disable_odoo_online",
        "portal_odoo_debranding",
    ]

    extra_modules = [m.strip() for m in args.modules.split(",") if m.strip()]
    all_modules = ",".join(base_modules + extra_modules)

    print(f"[1/3] Initializing database and installing modules: {all_modules} ...")
    cmd = [
        PYTHON_EXE,
        ODOO_BIN,
        "-c",
        ODOO_CONF,
        "-d",
        db_name,
        "-i",
        all_modules,
        "--stop-after-init",
    ]

    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"[ERROR] Failed to initialize database {db_name}. Return code: {res.returncode}")
        sys.exit(1)

    print("[2/3] Configuring tenant company and admin credentials...")
    config_script = f"""
import sys
sys.path.insert(0, r'{os.path.join(BASE_DIR, "odoo")}')
import odoo
from odoo.tools import config

config.parse_config(['-c', r'{ODOO_CONF}'])
registry = odoo.registry('{db_name}')

with registry.cursor() as cr:
    env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {{}})
    
    # 1. Update main company name
    company = env['res.company'].search([], limit=1)
    if company:
        company.write({{'name': '{args.company}'}})
    
    # 2. Update administrator account
    admin_user = env['res.users'].search([('login', '=', 'admin')], limit=1)
    if admin_user:
        admin_user.write({{
            'name': '{args.company} Admin',
            'login': '{args.admin_email}',
            'password': '{args.admin_password}',
            'email': '{args.admin_email}',
        }})
    
    # 3. Configure white-label branding parameters
    param_obj = env['ir.config_parameter'].sudo()
    param_obj.set_param('saas_whitelabel.app_name', '{args.brand_name}')
    param_obj.set_param('saas_whitelabel.company_url', 'https://yourcompany.com')
    param_obj.set_param('saas_whitelabel.support_url', 'https://yourcompany.com/support')
    param_obj.set_param('saas_whitelabel.documentation_url', 'https://yourcompany.com/docs')
    
    cr.commit()
    print('Tenant customization applied successfully.')
"""

    res2 = subprocess.run([PYTHON_EXE, "-c", config_script])
    if res2.returncode != 0:
        print("[WARNING] Tenant custom configuration encountered an issue.")
    else:
        print("[3/3] Tenant provisioning complete!")
        print("-" * 60)
        print(f"Tenant Name:     {args.company}")
        print(f"Database:        {db_name}")
        print(f"Admin Login:     {args.admin_email}")
        print(f"Admin Password:  {args.admin_password}")
        print(f"Direct URL:      http://localhost:8069/web?db={db_name}")
        print(f"Subdomain URL:   http://{db_name}.yourdomain.com:8069 (when dbfilter is active)")
        print("-" * 60)


if __name__ == "__main__":
    args = parse_args()
    provision_tenant(args)

