import pytest
from selene import browser, be


def test_github_mobile_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("This is a mobile resolution")
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_desktop_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("This is a desktop resolution")
    browser.open("https://github.com/")
    browser.element('[aria-label="Toggle navigation"].Button--link').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
