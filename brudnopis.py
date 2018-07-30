import pytest
from application import Application
from Config.cfg_att import Config


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login_logout(app):
    app.login(username=Config.username, password=Config.password)
    assert app.get_username_from_nav_bar() == Config.username
    app.wd.find_element_by_class_name("lastsubject").click()
    app.wd.find_element_by_id("logo").click()
    assert app.check_last_subject_name() == "udało się"