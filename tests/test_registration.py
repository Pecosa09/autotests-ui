import pytest

from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.mark.registration
@pytest.mark.regression
def test_successful_registration(registration_page:RegistrationPage,dashboard_page:DashboardPage):
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_page.fill_registration_form("pecosa@spam.com","pecosa","pecosa123")
    registration_page.click_registration_button()
    dashboard_page.check_visibility_dashboard_title()