import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_topic(app):
    topic_title = "new topic test"
    name = "Marcin"
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(name)
    app.create_new_topic(topic_title, topic_text="taki tam teścik")
    assert app.get_name_of_topic_title(topic_title) == topic_title
    app.topic_cleanup(topic_title)