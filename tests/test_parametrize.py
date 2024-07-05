import pytest
from selene import browser, be

github_mobile = pytest.mark.parametrize("platform_browser", ["320x568", "428x926"], indirect=True)

github_desktop = pytest.mark.parametrize("platform_browser", ["2560x1080", "1920x1080", "1280x1024"], indirect=True)


@github_mobile
def test_github_mobile(platform_browser):
    browser.open("https://github.com/")
    browser.element('[aria-label="Toggle navigation"].Button--link').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


@github_desktop
def test_github_desktop(platform_browser):
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
