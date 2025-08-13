from playwright.sync_api import sync_playwright

FIREFOX_EXECUTABLE_PATH="/home/ubuntu/.cache/ms-playwright/firefox-1489/firefox/firefox"

def main():
    with sync_playwright() as p:
        if FIREFOX_EXECUTABLE_PATH:
            browser = p.firefox.launch(executable_path=FIREFOX_EXECUTABLE_PATH)
        else:
            browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://www.flexjobs.com/", timeout=10000, wait_until="domcontentloaded")
        page.query_selector(f'a[href="https://www.flexjobs.com/"]')
        browser.close()

main()