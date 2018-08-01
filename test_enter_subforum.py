import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_enter_subforum_by_name(app):
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name("Marcin")
    assert app.wd.find_element_by_class_name('forum-title').text == 'Marcin'