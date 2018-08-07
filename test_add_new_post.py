import pytest
from application import Application
from Config.cfg_att import Config
import time


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_post(app):
    topic_title = app.random_string(10)
    name = "Marcin"
    reply = app.random_string(20)
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(name)
    app.create_new_topic(topic_title, topic_text = "kolejny tescik")
    app.post_a_reply(reply)
    assert app.get_post_content(reply) == reply
