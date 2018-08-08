import pytest
from application import Application
from Config.cfg_att import Config

# zapracuj na okejkę
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_private_message(app):
    temat_wiadomosci = app.random_string(10)
    tresc_wiadomosci = app.random_string(30)
    app.login(Config.username1, Config.password1)
    assert app.get_username_from_nav_bar() == Config.username1
    app.enter_private_messages()
    assert app.assert_if_user_in_private_messeges()
    app.send_private_message(temat_wiadomosci, tresc_wiadomosci)
    assert app.check_if_user_has_opened_newly_sent_message_in_outbox() ## ewentualnie check_if_user_in_newly_sent_message_in_outbox() ale dublowanie "in"
    app.enter_private_messages()
    app.enter_outbox()
    assert app.get_sent_message_title(temat_wiadomosci)
    """
    wiecej niz jeden taki temat wiadomosci -> sprawdz ile jest takich tematow przed i po ---> to be implemented later
    """
    app.logout()
    app.login(Config.username2, Config.password2)
    assert app.get_username_from_nav_bar() == Config.username2
    app.enter_private_messages()
    assert app.check_received_message(temat_wiadomosci)
    app.logout()
    app.login(Config.username1, Config.password1)
    app.enter_private_messages()
    app.enter_sent_messages()
    assert app.get_sent_message_title(temat_wiadomosci)
