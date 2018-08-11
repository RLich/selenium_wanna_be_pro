import pytest

from Config.cfg_att import Config
from pages.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_enter_subforum(app):
    # logowanie użytkownika i przejście do pierwszego subforum w indeksie
    app.login(Config.username1, Config.password1)
    app.nav_to_first_subforum()