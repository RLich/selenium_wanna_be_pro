import pytest

from Config.cfg_att import Config
from pages.application import Application


# zapracuj na okejkę
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_send_private_message(app):
    temat_wiadomosci = app.random_string(5, 10)
    tresc_wiadomosci = app.random_string(10, 30)

    app.login(Config.username2, Config.password2)
    app.enter_private_messages()
    wanted_titles = app.title_counter(temat_wiadomosci)
    app.logout()

    app.login(Config.username1, Config.password1)
    assert app.get_username_from_nav_bar() == Config.username1
    app.enter_private_messages()
    assert app.assert_if_user_in_private_messeges()
    app.send_private_message(temat_wiadomosci, tresc_wiadomosci)
    app.enter_priv_msg_tab("outbox")
    assert app.check_message_title(temat_wiadomosci)
    app.logout()

    app.login(Config.username2, Config.password2)
    assert app.get_username_from_nav_bar() == Config.username2
    app.enter_private_messages()
    assert len(app.title_counter(temat_wiadomosci)) == len(wanted_titles) + 1
    app.logout()

    app.login(Config.username1, Config.password1)
    app.enter_private_messages()
    app.enter_sent_messages()
    assert app.check_message_title(temat_wiadomosci)
