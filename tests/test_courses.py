from playwright.sync_api import sync_playwright, expect



def test_empty_courses_list():
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        context = chromium.new_context()
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        email_input = page.get_by_test_id("registration-form-email-input").locator("input")
        username_input = page.get_by_test_id("registration-form-username-input").locator("input")
        password_input = page.get_by_test_id("registration-form-password-input").locator("input")
        registration_button = page.get_by_test_id("registration-page-registration-button")
        dashboard = page.get_by_test_id("dashboard-toolbar-title-text")

        email_input.fill("user.name@gmail.com")
        username_input.fill("username")
        password_input.fill("password")
        registration_button.click()
        context.storage_state(path='browser-state.json')

    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        context = chromium.new_context(storage_state='browser-state.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        section_title = page.get_by_test_id("courses-list-toolbar-title-text")
        block_icon = page.get_by_test_id("courses-list-empty-view-icon")
        block_title = page.get_by_test_id("courses-list-empty-view-title-text")
        block_description = page.get_by_test_id("courses-list-empty-view-description-text")

        expect(section_title).to_be_visible()
        expect(section_title).to_have_text('Courses')

        expect(block_icon).to_be_visible()

        expect(block_title).to_be_visible()
        expect(block_title).to_have_text('There is no results')

        expect(block_description).to_be_visible()
        expect(block_description).to_have_text('Results from the load test pipeline will be displayed here')
