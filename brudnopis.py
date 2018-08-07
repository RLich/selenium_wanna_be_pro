import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_private_message(app):
    temat_wiadomosci = "testowy temat"
    tresc_wiadomosci = "testowa wiadomość"
    prefix = "test"
    app.login(Config.username1, Config.password1)
    assert app.get_username_from_nav_bar() == Config.username1
    print("udalo sie")
    print (app.random_string(prefix, 15))




