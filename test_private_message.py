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
    kutang = app.random_string(10)
    tresc_wiadomosci = app.random_string(30)
    app.login(Config.username2, Config.password2)
    app.enter_private_messages()

    chuju = app.title_kutas(kutang)  #  return lista
"""

chuju: List<String> = app.title_kutas(kutang)
tresc: String = "xfafafafa"
tresc_random: String = app.random(131)
fun title_kusta(temat_wiad): List<String>{ciało  return List<String>}

fun zaloguj(){.clicka()}

"""
    app.logout()
    app.login(Config.username1, Config.password1)
    assert app.get_username_from_nav_bar() == Config.username1
    app.enter_private_messages()
    assert app.assert_if_user_in_private_messeges()

    app.send_private_message(kutang, tresc_wiadomosci)

    app.logout()
    app.login(Config.username2, Config.password2)
    assert app.get_username_from_nav_bar() == Config.username2
    app.enter_private_messages()
     # chuju = []
    assert len(app.title_kutas(kutang)) == len(chuju) + 1

    app.enter_priv_msg_tab("outbox")

    app.logout()
    app.login(Config.username1, Config.password1)
    app.enter_private_messages()
    app.enter_sent_messages()
    app.title_counter_after(kutang)
    assert len(chuju) == len(app.title_kutas(kutang)) + 1






    assert app.wanted_titles
