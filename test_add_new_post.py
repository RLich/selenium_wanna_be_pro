import pytest

from Config.cfg_att import Config
from pages.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_post(app):
    topic_title = app.random_string(10)
    subforum_name = "Marcin"
    topic_text = app.random_string(30)
    reply = app.random_string(20)
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(subforum_name)
    app.create_new_topic(topic_title, topic_text)
    app.post_a_reply(reply)
    assert app.get_post_content(reply) == reply
