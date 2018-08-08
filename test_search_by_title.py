import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_earch_by_title(app):
    topic_title = "Unikalny temat dla testu wyszukiwarki"
    topic_text = app.random_string(30)
    subforum_name = "Rafał"
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(subforum_name)
    app.create_new_topic(topic_title, topic_text)
    app.search_by_title(topic_title)
    assert app.check_highlighted_topic_title()