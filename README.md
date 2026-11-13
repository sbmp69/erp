# CloudERP — White-Labeled Multi-Tenant SaaS Platform

An enterprise-ready, white-labeled multi-tenant SaaS ERP built on top of Odoo 18.0 Community Edition.

---

## Features

- **Full White-Labeling**: Custom brand name, custom logo, custom favicon, debranded login screen, debranded portal, and debranded transactional email templates.
- **Dynamic Web Title**: Owl JavaScript service patch keeps window titles synchronized with your SaaS platform brand (`CloudERP`) instead of Odoo.
- **Cleaned User Navigation**: Odoo Account and upsell links removed; replaced with custom knowledge base and customer support URLs.
- **Enterprise Debranding**: Integrated OCA `server-brand` modules (`remove_odoo_enterprise`, `disable_odoo_online`, `portal_odoo_debranding`) to strip all enterprise banners, upgrade notices, and telemetry.
- **Multi-Tenant SaaS Routing**: Native database filtering (`dbfilter = ^%d$`) routes subdomains (e.g. `clienta.yourdomain.com`) to isolated client databases.
- **Automated Tenant Onboarding**: CLI script `provision_tenant.py` for one-command tenant database creation, branding injection, and module installation.

---

## Directory Structure

```
├── custom_addons/
│   ├── saas_whitelabel/      # Custom SaaS white-label & debranding addon
│   └── server_brand/         # OCA debranding addons (remove_odoo_enterprise, etc.)
├── odoo/                     # Odoo 18.0 Community core source
├── odoo.conf                 # Odoo server configuration
├── provision_tenant.py       # SaaS tenant provisioning CLI
├── requirements-win.txt      # Windows Python requirements
├── start_odoo.bat            # 1-click startup script for Windows
├── stop_odoo.bat             # 1-click stop script for Windows
└── .gitignore
```

---

## Quick Start (Local Development)

### 1. Requirements
- Python 3.10 or 3.11 (64-bit)
- PostgreSQL 14, 15, or 16

### 2. Install Dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements-win.txt
```

### 3. Launch the ERP
```cmd
start_odoo.bat
```
Visit **http://localhost:8069** in your browser.

---

## SaaS Tenant Provisioning

Provision an isolated tenant database on the fly:
```bash
python provision_tenant.py --tenant acme --company "Acme Corp" --admin-email "admin@acme.com" --admin-password "secret123" --brand-name "CloudERP"
```

---

## Production Deployment (Nginx Reverse Proxy)

In production, run behind Nginx with wildcard subdomains (`*.yourdomain.com`) and set `dbfilter = ^%d$` in `odoo.conf` to automatically route incoming tenant subdomains to their dedicated databases.
