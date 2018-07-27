from selenium.webdriver.chrome.webdriver import WebDriver
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_site_title(app):
    app.open_home_page()
    app.get_site_title.assertIn("ATT Nauka - Index page", app.get_site_title)