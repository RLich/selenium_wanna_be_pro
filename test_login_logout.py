import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login_logout(app):
    app.login(username=Config.username1, password=Config.password1)
    assert app.get_username_from_nav_bar() == Config.username1
    app.logout()
    assert app.get_login_from_nav_bar() == "Login"