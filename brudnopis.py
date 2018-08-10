import pytest

from Config.cfg_att import Config
from pages.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_glupoty(app):
    subforum_name = "Rafał"
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(subforum_name)
