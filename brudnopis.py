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
    topic_title = "new topic test"
    name = "Konrad"
    app.login(Config.username, Config.password)
    app.enter_subforum_by_name(name)
    assert app.wd.find_element_by_class_name('forum-title').text == name
    time.sleep(1)
    app.create_new_topic(topic_title, topic_text = "kolejny tescik")
    time.sleep(1)
    assert app.get_last_subject_name() == topic_title
    app.topic_cleanup()