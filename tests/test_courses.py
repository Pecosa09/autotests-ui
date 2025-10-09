from playwright.sync_api import sync_playwright, expect
import pytest



@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
        chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
        section_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
        block_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
        block_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
        block_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")

        expect(section_title).to_be_visible()
        expect(section_title).to_have_text('Courses')

        expect(block_icon).to_be_visible()

        expect(block_title).to_be_visible()
        expect(block_title).to_have_text('There is no results')

        expect(block_description).to_be_visible()
        expect(block_description).to_have_text('Results from the load test pipeline will be displayed here')
