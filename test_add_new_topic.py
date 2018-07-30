import pytest
from application import Application
from Config.cfg_att import Config
import time


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_topic(app):
    app.login(Config.username, Config.password)
    app.enter_subforum_by_name(name="Rafał")
    assert app.wd.find_element_by_class_name('forum-title').text == 'Rafał'
    app.create_new_topic(topic_title = "kolejny test", topic_text = "kolejny teścik")

    assert app.check_last_subject_name() == "topic_title"

