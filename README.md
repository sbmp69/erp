# ConneuralERP — The All-in-One Business Operating System

An enterprise-grade, modern business management and ERP platform engineered by **Conneural Technologies** to streamline daily operations, automate workflows, and accelerate business growth.

---

## Overview

**ConneuralERP** is a complete, unified operating system designed for modern businesses — from growing startups, restaurants, and retail shops to mid-sized enterprises. Instead of juggling multiple disconnected subscriptions (CRM, invoicing software, warehouse tracking, and POS systems), ConneuralERP centralizes your entire company into one seamless, intuitive workspace.

- **Unified Daily Operations**: Manage leads, quotes, inventory, invoices, and payments in one connected workflow without manual data entry.
- **Retail & Restaurant Ready**: Includes complete Point of Sale, visual table floor plans, kitchen order tickets (KOT), and touchless customer mobile QR self-ordering.
- **Smart Inventory & Procurement**: Automated replenishment, stock tracking, multi-warehouse management, and supplier bills.
- **Automated Billing & Accounting**: Instant invoice generation from sales orders, payment registration, bank tracking, and real-time financial reporting.
- **Projects & Team Collaboration**: Track tasks, milestones, employee profiles, and internal team communication.
- **Scalable Multi-Tenant Architecture**: Cloud-ready database-per-organization architecture with automated client onboarding (`provision_tenant.py`).
- **Smooth & Distraction-Free Experience**: Built-in client shielding and security protection for uninterrupted daily performance.

---

## Core Capabilities

| Solution | What It Does For Your Business |
| :--- | :--- |
| **Sales & CRM** | Visual lead pipeline, quotation builder, automatic order confirmations, and customer portal |
| **Invoicing & Finance** | Professional invoicing, recurring billing, payment tracking, and ledger accounting |
| **Point of Sale & Dining** | Fast cashier checkout, visual table management, and customer smartphone QR ordering |
| **Inventory & Supply Chain** | Real-time stock levels, incoming shipments, delivery validation, and supplier management |
| **Project & Task Tracking** | Kanban task boards, milestone tracking, and cross-department collaboration |
| **HR & Team Management** | Centralized employee directory, departments, and onboarding workflows |

---

## Directory Layout

```
├── custom_addons/
│   ├── saas_whitelabel/      # ConneuralERP brand identity & core platform extensions
│   └── server_brand/         # Enterprise security & optimization modules
├── odoo/                     # Core open-source ERP engine
├── odoo.conf                 # ConneuralERP runtime configuration
├── test_suite.py             # 35-point automated QA & workflow verification suite
├── provision_tenant.py       # Instant organization onboarding CLI
├── requirements-win.txt      # Platform dependencies
├── start_odoo.bat            # One-click startup script
├── stop_odoo.bat             # One-click shutdown script
└── .gitignore
```

---

## Quick Launch (Local Setup)

1. Launch PostgreSQL and ConneuralERP:
   ```cmd
   start_odoo.bat
   ```
2. Open your browser and navigate to: **http://localhost:8069**
3. Default credentials:
   - **Login**: `admin`
   - **Password**: `admin`

---

## Onboarding a New Organization

To provision a fresh, isolated workspace for a new business client:
```cmd
python provision_tenant.py --tenant acme --company "Acme Corp" --admin-email "admin@acme.com" --admin-password "secret123"
```

---

## System Verification

To run the complete 35-point automated workflow verification suite:
```cmd
python test_suite.py
```

---

## Production Deployment

Configure your reverse proxy (Nginx / Traefik / Caddy) with wildcard domain routing (`*.conneural.com`) proxying to port `8069`, with `dbfilter = ^%d$` in `odoo.conf` for seamless organization subdomains.
