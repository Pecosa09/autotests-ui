
from playwright.sync_api import sync_playwright
with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    login_button = page.locator('//button[@data-testid="login-page-login-button"]')
    error_message = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    email_input.fill("user.name@gmail.com")
    password_input.fill("Password")
    
