import pytest
from application import Application
from Config.cfg_att import Config
# nie ma okejki, ale blisko!

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_topic(app):
    topic_title = app.random_string(10)
    topic_text = app.random_string(30)
    subforum_name = "Marcin"
    app.login(Config.username1, Config.password1)
    app.enter_subforum_by_name(subforum_name)
    app.create_new_topic(topic_title, topic_text)
    app.open_home_page()
    app.enter_subforum_by_name(subforum_name)
    # get_list_of_topic_titles().shouldContainIgnoringCase(topic_title)
    # wez nazwe z tytułu tematu ( x ) czy jest równa tytłowi tematu ( x )
    assert app.check_title_in_topic_titles(topic_title) == topic_title