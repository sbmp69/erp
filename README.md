# ConneuralERP — White-Labeled Multi-Tenant SaaS Platform

An enterprise-grade, fully white-labeled multi-tenant SaaS ERP engineered by Conneural Technologies.

---

## Overview

ConneuralERP is a complete commercial SaaS platform delivering core business intelligence, operations, CRM, manufacturing, Point of Sale, and accounting without proprietary licensing dependencies.

- **100% White-Labeled**: Debranded client UI, custom brand names, custom vectors and favicons, debranded login screens, and custom notification templates.
- **Enterprise Upsell Protection**: Remote cloud upsells and proprietary dependencies blocked at the ORM layer.
- **Multi-Tenant SaaS Engine**: Native subdomain-to-database routing via PostgreSQL database-per-tenant architecture (`dbfilter = ^%d$`).
- **Instant Tenant Provisioning**: Automated onboarding CLI (`provision_tenant.py`) creates new client databases in seconds.
- **Extension Shielding**: Silences third-party browser extensions (MetaMask, Honey, etc.) from triggering client errors.

---

## Directory Layout

```
├── custom_addons/
│   ├── saas_whitelabel/      # ConneuralERP branding, debranding & shielding engine
│   └── server_brand/         # OCA server branding suite
├── odoo/                     # Core open-source engine
├── odoo.conf                 # ConneuralERP server configuration
├── provision_tenant.py       # Multi-tenant onboarding CLI
├── requirements-win.txt      # Runtime dependencies
├── start_odoo.bat            # One-click startup script
├── stop_odoo.bat             # One-click shutdown script
└── .gitignore
```

---

## Quick Launch (Local)

1. Launch PostgreSQL and ConneuralERP:
   ```cmd
   start_odoo.bat
   ```
2. Navigate to: **http://localhost:8069**
3. Default credentials:
   - **Login**: `admin`
   - **Password**: `admin`

---

## Provisioning a New Tenant

To spin up a new isolated client database:
```cmd
python provision_tenant.py --tenant acme --company "Acme Corp" --admin-email "admin@acme.com" --admin-password "secret123"
```

---

## Production Deployment

Configure your reverse proxy (Nginx/Traefik) with wildcard routing (`*.conneural.com`) directing to port `8069`, with `dbfilter = ^%d$` in `odoo.conf`.
