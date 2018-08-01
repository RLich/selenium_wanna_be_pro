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
    name = "Marcin"
    reply = "test reply"
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(name)
    app.wd.find_element_by_class_name("topictitle").click()
    assert app.get_post_content(reply) == reply
    app.post_and_topic_cleanup()