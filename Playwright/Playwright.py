from playwright.sync_api import sync_playwright

site = input("site: ")

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)
    #browser = p.firefox.launch()
    page = browser.new_page()
    page.goto(site)
    print(page.title())
    browser.close()
