#!/usr/bin/env python3
"""Generate Zoom background image from HTML"""

import os
from playwright.sync_api import sync_playwright

def generate_zoom_background():
    """Convert HTML to PNG image for Zoom background"""
    html_path = os.path.join(os.path.dirname(__file__), 'zoom-background.html')
    output_path = os.path.join(os.path.dirname(__file__), 'zoom-background.png')

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        page.goto(f'file://{html_path}')
        page.screenshot(path=output_path, full_page=False)
        browser.close()

    print(f"Zoom background created: {output_path}")

if __name__ == '__main__':
    generate_zoom_background()
