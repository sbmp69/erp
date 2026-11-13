/** @odoo-module **/

import { registry } from "@web/core/registry";
import { session } from "@web/session";

const serviceRegistry = registry.category("services");
const originalTitleService = serviceRegistry.get("title");

export const saasTitleService = {
    ...originalTitleService,
    start(env) {
        const service = originalTitleService ? originalTitleService.start(env) : {};
        const originalSetParts = service.setParts;
        const getBrandName = () => session.saas_brand_name || "CloudERP";

        if (originalSetParts) {
            service.setParts = function (parts) {
                if (parts) {
                    for (const key in parts) {
                        if (typeof parts[key] === "string") {
                            parts[key] = parts[key].replace(/\bOdoo\b/gi, getBrandName());
                        }
                    }
                }
                originalSetParts.call(this, parts);
                if (document.title.includes("Odoo")) {
                    document.title = document.title.replace(/\bOdoo\b/gi, getBrandName());
                } else if (!document.title || document.title === "Odoo") {
                    document.title = getBrandName();
                }
            };
        }

        // Keep page title synchronized with the SaaS brand name
        const cleanTitle = () => {
            const brand = getBrandName();
            if (document.title.includes("Odoo")) {
                document.title = document.title.replace(/\bOdoo\b/gi, brand);
            }
        };

        // Clean initial title and listen for modifications
        cleanTitle();
        if (typeof MutationObserver !== "undefined") {
            const titleEl = document.querySelector("title");
            if (titleEl) {
                const observer = new MutationObserver(() => {
                    const brand = getBrandName();
                    if (document.title.includes("Odoo")) {
                        document.title = document.title.replace(/\bOdoo\b/gi, brand);
                    }
                });
                observer.observe(titleEl, { subtree: true, characterData: true, childList: true });
            }
        }

        return service;
    },
};

serviceRegistry.add("title", saasTitleService, { force: true });

