"""
ConneuralERP Brand Asset & Logo Synchronization Engine
======================================================
Propagates the official Conneural logo and mark across:
1. saas_whitelabel static assets (logo, dark logo, favicon, PWA icons)
2. Core fallback web assets (web/static/img, point_of_sale/static/src/img)
3. Bot avatars (mail/static/src/img/odoobot.png)
4. PostgreSQL Database models (res.company, res.partner, website, ConneuralBot)
5. Tenant provisioning script
"""

import os
import sys
import io
import base64
from PIL import Image

BASE_DIR = r"E:\ERP"
SRC_IMAGE = r"C:\Users\Meet\.gemini\antigravity\brain\2dd5c042-fbf5-4931-94c6-1c9c97920349\.user_uploaded\media_1794748645755_4df03b65.png"

def process_branding():
    print(f"Loading source logo from: {SRC_IMAGE}")
    im = Image.open(SRC_IMAGE).convert('RGBA')

    # 1. Generate Full Logo (cropped tightly with balanced 12px padding)
    bbox = im.getbbox()
    pad = 12
    crop_box = (
        max(0, bbox[0] - pad),
        max(0, bbox[1] - pad),
        min(im.width, bbox[2] + pad),
        min(im.height, bbox[3] + pad)
    )
    full_logo = im.crop(crop_box)
    print(f"Full logo dimensions: {full_logo.size[0]}x{full_logo.size[1]}")

    # Full logo byte buffers
    full_logo_buf = io.BytesIO()
    full_logo.save(full_logo_buf, format="PNG", optimize=True)
    full_logo_bytes = full_logo_buf.getvalue()
    full_logo_b64 = base64.b64encode(full_logo_bytes).decode('utf-8')

    # 2. Generate Square Icon Mark (the 'C' + neural 'N' mark on the left)
    icon_crop_box = (15, 37, 272, 312)
    icon_raw = im.crop(icon_crop_box)
    
    # Place on 512x512 transparent canvas with 15% inner padding
    canvas_dim = 512
    target_inner = int(canvas_dim * 0.82)
    # Scale icon maintaining aspect ratio
    scale = min(target_inner / icon_raw.width, target_inner / icon_raw.height)
    new_w = int(icon_raw.width * scale)
    new_h = int(icon_raw.height * scale)
    icon_scaled = icon_raw.resize((new_w, new_h), Image.Resampling.LANCZOS)

    square_icon = Image.new('RGBA', (canvas_dim, canvas_dim), (0, 0, 0, 0))
    pos_x = (canvas_dim - new_w) // 2
    pos_y = (canvas_dim - new_h) // 2
    square_icon.paste(icon_scaled, (pos_x, pos_y), icon_scaled)
    print(f"Square mark icon dimensions: {square_icon.size[0]}x{square_icon.size[1]}")

    square_icon_buf = io.BytesIO()
    square_icon.save(square_icon_buf, format="PNG", optimize=True)
    square_icon_bytes = square_icon_buf.getvalue()
    square_icon_b64 = base64.b64encode(square_icon_bytes).decode('utf-8')

    # 3. Generate multi-resolution .ico (16, 32, 48, 64, 128, 256)
    ico_buf = io.BytesIO()
    square_icon.save(
        ico_buf,
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    )
    ico_bytes = ico_buf.getvalue()

    # 4. Generate SVG wrappers
    full_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {full_logo.width} {full_logo.height}" width="100%" height="100%">
  <image width="{full_logo.width}" height="{full_logo.height}" href="data:image/png;base64,{full_logo_b64}"/>
</svg>'''.encode('utf-8')

    icon_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%">
  <image width="512" height="512" href="data:image/png;base64,{square_icon_b64}"/>
</svg>'''.encode('utf-8')

    # 5. PWA Resized Icons
    icon_192 = square_icon.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192_buf = io.BytesIO()
    icon_192.save(icon_192_buf, format="PNG", optimize=True)
    icon_192_bytes = icon_192_buf.getvalue()

    icon_ios = square_icon.resize((180, 180), Image.Resampling.LANCZOS)
    icon_ios_buf = io.BytesIO()
    icon_ios.save(icon_ios_buf, format="PNG", optimize=True)
    icon_ios_bytes = icon_ios_buf.getvalue()

    icon_tiny = square_icon.resize((64, 64), Image.Resampling.LANCZOS)
    icon_tiny_buf = io.BytesIO()
    icon_tiny.save(icon_tiny_buf, format="PNG", optimize=True)
    icon_tiny_bytes = icon_tiny_buf.getvalue()

    # -------------------------------------------------------------------------
    # Target Destination Mapping
    # -------------------------------------------------------------------------
    targets = {
        # Full Logo destinations
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "logo.png"): full_logo_bytes,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "logo_dark.png"): full_logo_bytes,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "logo_full.png"): full_logo_bytes,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "description", "icon.png"): square_icon_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "logo.png"): full_logo_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "logo2.png"): full_logo_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "logo_inverse_white_206px.png"): full_logo_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "point_of_sale", "static", "src", "img", "logo.png"): full_logo_bytes,
        
        # Favicon destinations
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "favicon.ico"): ico_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "favicon.ico"): ico_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "src", "img", "favicon.ico"): ico_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "point_of_sale", "static", "src", "img", "favicon.ico"): ico_bytes,

        # SVG Logo destinations
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "odoo_logo.svg"): full_svg,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "odoo_logo_dark.svg"): full_svg,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "odoo-icon.svg"): icon_svg,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo_logo.svg"): full_svg,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo_logo_dark.svg"): full_svg,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo-icon.svg"): icon_svg,

        # PWA & Mobile icons
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "odoo-icon-192x192.png"): icon_192_bytes,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "odoo-icon-512x512.png"): square_icon_bytes,
        os.path.join(BASE_DIR, "custom_addons", "saas_whitelabel", "static", "src", "img", "odoo-icon-ios.png"): icon_ios_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo-icon-192x192.png"): icon_192_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo-icon-512x512.png"): square_icon_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo-icon-ios.png"): icon_ios_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web", "static", "img", "odoo_logo_tiny.png"): icon_tiny_bytes,

        # ConneuralBot avatars
        os.path.join(BASE_DIR, "odoo", "addons", "mail", "static", "src", "img", "odoobot.png"): square_icon_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "mail", "static", "src", "img", "odoobot_transparent.png"): square_icon_bytes,
        os.path.join(BASE_DIR, "odoo", "addons", "web_editor", "static", "src", "img", "odoobot_transparent.png"): square_icon_bytes,
    }

    print("\nWriting physical image assets across codebase:")
    for filepath, data in targets.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "wb") as f:
            f.write(data)
        print(f"  -> Written: {filepath} ({len(data)} bytes)")

    # -------------------------------------------------------------------------
    # 6. Database Model Synchronization via Odoo ORM
    # -------------------------------------------------------------------------
    print("\nSynchronizing Database records (res.company, res.partner, website, ConneuralBot)...")
    sys.path.insert(0, os.path.join(BASE_DIR, "odoo"))
    import odoo
    from odoo.tools import config

    config.parse_config(["-c", os.path.join(BASE_DIR, "odoo.conf"), "-d", "odoo"])
    odoo.netsvc.init_logger()
    registry = odoo.registry("odoo")

    with registry.cursor() as cr:
        env = odoo.api.Environment(cr, odoo.SUPERUSER_ID, {})

        # 1. Update Company Logo (displays on invoices, quotations, reports, portal)
        companies = env['res.company'].search([])
        for comp in companies:
            comp.write({
                'logo': full_logo_b64,
                'logo_web': full_logo_b64,
            })
            if comp.partner_id:
                comp.partner_id.write({'image_1920': full_logo_b64})
            print(f"  -> Updated Company ID {comp.id} ('{comp.name}') logo")

        # 2. Update Website Logo
        if 'website' in env:
            websites = env['website'].search([])
            for site in websites:
                site.write({'logo': full_logo_b64})
                print(f"  -> Updated Website ID {site.id} ('{site.name}') logo")

        # 3. Update ConneuralBot Avatar
        bot_partner = env.ref('base.partner_root', raise_if_not_found=False)
        if bot_partner:
            bot_partner.write({
                'name': 'ConneuralBot',
                'image_1920': square_icon_b64,
                'image_1024': square_icon_b64,
                'image_512': square_icon_b64,
                'image_256': square_icon_b64,
                'image_128': square_icon_b64,
            })
            print(f"  -> Updated ConneuralBot avatar (Partner ID {bot_partner.id})")

        cr.commit()
        print("Database logo update committed successfully!")

    print("\nAll Conneural brand logos & icons successfully deployed everywhere!")

if __name__ == "__main__":
    process_branding()
