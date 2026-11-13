/** @odoo-module **/

import { registry } from "@web/core/registry";
import { session } from "@web/session";

const serviceRegistry = registry.category("services");
const originalTitleService = serviceRegistry.get("title");

// 1. Instantly rewrite URL path to clean /app prefix if /odoo is present
if (typeof window !== "undefined" && window.location) {
    if (window.location.pathname === "/odoo" || window.location.pathname.startsWith("/odoo/")) {
        const cleanPath = window.location.pathname.replace(/^\/odoo/, "/app") + window.location.search + window.location.hash;
        try {
            window.history.replaceState(null, "", cleanPath);
        } catch (e) {
            // Ignore if restricted
        }
    }
}

export const saasTitleService = {
    ...originalTitleService,
    start(env) {
        const service = originalTitleService ? originalTitleService.start(env) : {};
        const originalSetParts = service.setParts;
        const getBrandName = () => session.saas_brand_name || "ConneuralERP";

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

                // Ensure URL keeps clean /app prefix
                if (window.location.pathname.startsWith("/odoo")) {
                    const clean = window.location.pathname.replace(/^\/odoo/, "/app") + window.location.search + window.location.hash;
                    window.history.replaceState(null, "", clean);
                }
            };
        }

        // Keep page title synchronized with ConneuralERP brand name
        const cleanTitle = () => {
            const brand = getBrandName();
            if (document.title.includes("Odoo")) {
                document.title = document.title.replace(/\bOdoo\b/gi, brand);
            }
        };

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
