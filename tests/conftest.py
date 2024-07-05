import pytest
from selene import browser


@pytest.fixture(params=["320x568", "428x926"])
def mobile_browser(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=["2560x1080", "1920x1080", "1280x1024"])
def desktop_browser(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=["320x568", "428x926", "2560x1080", "1920x1080", "1280x1024"])
def platform_browser(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=["320x568", "428x926", "2560x1080", "1920x1080", "1280x1024"])
def setup_browser(request):
    width, height = map(int, request.param.split("x"))
    browser.config.window_width = width
    browser.config.window_height = height
    if request.param in ["2560x1080", "1920x1080", "1280x1024"]:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
