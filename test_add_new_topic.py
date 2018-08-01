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
    name = "Konrad"
    topic_title = "new topic test"
    app.login(Config.username, Config.password)
    app.enter_subforum_by_name(name)
    assert app.wd.find_element_by_class_name('forum-title').text == name
    app.create_new_topic(topic_title, topic_text = "kolejny teścik")
    assert app.get_last_subject_name() == topic_title
    app.topic_cleanup()
    time.sleep(5)
    app.wd.find_element_by_id("logo").click()
    assert app.get_last_subject_name() != topic_title