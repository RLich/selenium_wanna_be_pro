import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_brudnopisowy(app):
    topic = app.wd.find_element_by_class_name("topictitle")
    app.login(Config.username2, Config.password2)
    app.enter_private_messages()
    print(app.get_topics_number().count(topic))



