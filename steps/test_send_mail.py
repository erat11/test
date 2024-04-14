import pytest
import pytest_bdd
from playwright.sync_api import sync_playwright
from pytest_bdd import given, when, then

from config.send_mail_config import *
from locators.send_mail_locators import *

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


#Login--------------------------------------------

@pytest.fixture
@given("I am on the email login page")
def navigate_to_login_page(page):
    page.goto(LOGIN_ADDRESS)


@when("I enter my email address and password")
def enter_credentials(page):
    page.fill( usernameL, EMAIL)
    page.fill( passwordL, PASSWORD )


@when("I click on the login button")
def click_login_button(page):
    page.click( loginButtonL )


#Logout--------------------------------------------


@given("I am logged in and see my inbox")
@then("I should be redirected to the inbox")
def should_be_in_inbox(page):
    assert page.url == INBOX_ADDRESS


@when("I press my profile button and logout")
def logout(page):
    page.click( profileButtonL )
    page.click( signoutButtonL )


@then("I should be redirected to the login site")
def should_be_on_login_page(page):
    assert page.url == LOGIN_ADDRESS


#Send Mail--------------------------------------------

@when("I click on the new message button")
def click_contacts_and_compose(page):
    page.click( composeL )


@when("I fill in the recipient, subject and attach a file")
def fill_in_details(page):
    page.fill( emailFillL, EMAIL)
    page.fill( subjectFillL, "Test SUBJECT" )
    page.setInputFiles('input[type="file"]', PATH_TO_ATTACHED_FILE )

@then("I click the send button")
def click_send(page):
    page.click( sendL )


