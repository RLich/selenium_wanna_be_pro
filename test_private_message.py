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
    assert app.assert_if_user_in_private_messeges() == "New PM"
    app.send_private_message(temat_wiadomosci, tresc_wiadomosci)
    assert app.assert_if_information_window_present() == "Information"
    assert app.assert_if_user_redirected_to_sent_message() == 'Return to “Outbox”'
    app.enter_outbox_from_newly_sent_message()
    assert app.assert_sent_message(temat_wiadomosci) == temat_wiadomosci
    app.logout()
    app.login(Config.username2, Config.password2)
    assert app.get_username_from_nav_bar() == Config.username2
    app.enter_private_messages()
    assert app.assert_received_message(temat_wiadomosci) == temat_wiadomosci
    app.logout()
    app.login(Config.username1, Config.password1)
    app.enter_private_messages()
    app.enter_sent_messages()
    assert app.assert_sent_message(temat_wiadomosci) == temat_wiadomosci

