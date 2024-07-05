"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

@pytest.fixture(params=[(набор размеров экранов)])
def setup_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width > 900:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()

# test_github_skip.py
def test_mobile_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Это мобилное разрешение")
    browser.open("https://github.com/")
    ...

def test_desktop_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open("https://github.com/")

def test_github_desktop():
    pass


def test_github_mobile():
    pass