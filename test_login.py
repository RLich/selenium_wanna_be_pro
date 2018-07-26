import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    app.login(username=Config.username, password=Config.password)
    app.logout()