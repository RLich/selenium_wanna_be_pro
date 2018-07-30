import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_enter_subforum_by_name(app):
    app.login(username="rafal", password="rafaltestowy")
    app.enter_subforum_by_name(name="Marcin")
    assert app.wd.find_element_by_class_name('forum-title').text == 'Marcin'

