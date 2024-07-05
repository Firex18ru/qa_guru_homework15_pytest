import pytest
from selene import browser, be


@pytest.fixture(params=["2560x1080", "1920x1080", "1280x1024"])
def desktop_browser(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


def test_github_mobile(mobile_browser):
    browser.open("https://github.com/")
    browser.element('[aria-label="Toggle navigation"].Button--link').click()
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()


def test_github_desktop():
    browser.open("https://github.com/")
    browser.element(".HeaderMenu-link--sign-in").should(be.clickable).click()
    pass
