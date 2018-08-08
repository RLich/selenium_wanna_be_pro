import pytest
from application import Application
from Config.cfg_att import Config


# jest okejka


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_enter_subforum_by_name(app):
    name_of_subforum = "Marcin"
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(name_of_subforum)
    assert app.check_subforum_name(name_of_subforum)
