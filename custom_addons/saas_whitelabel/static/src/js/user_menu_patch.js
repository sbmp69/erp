/** @odoo-module **/

import { registry } from "@web/core/registry";
import { session } from "@web/session";
import { browser } from "@web/core/browser/browser";
import { _t } from "@web/core/l10n/translation";

const userMenuRegistry = registry.category("user_menuitems");

// Remove default Odoo Account entry
if (userMenuRegistry.contains("odoo_account")) {
    userMenuRegistry.remove("odoo_account");
}

// Remove default Odoo documentation
if (userMenuRegistry.contains("documentation")) {
    userMenuRegistry.remove("documentation");
}

// Add custom SaaS Documentation
userMenuRegistry.add(
    "saas_documentation",
    (env) => {
        const url = session.saas_documentation_url || "https://yourcompany.com/docs";
        return {
            type: "item",
            id: "saas_documentation",
            description: _t("Documentation"),
            href: url,
            callback: () => {
                browser.open(url, "_blank");
            },
            sequence: 10,
        };
    },
    { sequence: 10 }
);

// Remove default Odoo support
if (userMenuRegistry.contains("support")) {
    userMenuRegistry.remove("support");
}

// Add custom SaaS Support
userMenuRegistry.add(
    "saas_support",
    (env) => {
        const url = session.saas_support_url || "https://yourcompany.com/support";
        return {
            type: "item",
            id: "saas_support",
            description: _t("Support & Helpdesk"),
            href: url,
            callback: () => {
                browser.open(url, "_blank");
            },
            sequence: 20,
        };
    },
    { sequence: 20 }
);

