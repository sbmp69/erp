/** @odoo-module **/

/**
 * Filter out unhandled promise rejections originating from third-party browser extensions
 * (such as MetaMask, Honey, crypto wallets, ad-blockers) so they don't trigger Odoo's
 * "Oops! Something went wrong" error dialog.
 */
if (typeof window !== "undefined") {
    window.addEventListener(
        "unhandledrejection",
        (event) => {
            const reason = event.reason;
            const text = (reason && (reason.stack || reason.message || String(reason))) || "";
            if (
                text.includes("chrome-extension://") ||
                text.includes("moz-extension://") ||
                text.includes("MetaMask") ||
                text.includes("inpage.js") ||
                text.includes("nkbihfbeogaeaoehlefnkodbefgpgknn")
            ) {
                // Silently prevent third-party extension error from bubbling to Odoo crash manager
                event.preventDefault();
                event.stopImmediatePropagation();
            }
        },
        true // Capture phase: intercepts before Odoo's error listener
    );
}

