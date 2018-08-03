import pytest
from application import Application
from Config.cfg_att import Config
import time


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_private_message(app):
    temat_wiadomosci = "testowy temat"
    tresc_wiadomosci = "testowa wiadomość"
    app.login(Config.username1, Config.password1)
    assert app.get_username_from_nav_bar() == Config.username1
    app.enter_private_messages()
    app.enter_outbox()
    time.sleep(1)
    app.enter_sent_messages()
    time.sleep(3)