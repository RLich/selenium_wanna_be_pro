import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_brudnopis(app):
    app.login(Config.username2, Config.password2)
    app.enter_private_messages()
    list_of_topics = app.wd.find_elements_by_class_name("topictitle")
    print(len(list_of_topics.count("topictitle")))