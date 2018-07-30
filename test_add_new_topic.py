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
    app.login(Config.username, Config.password)
    app.enter_subforum_by_name(name="Marcin")
    assert app.wd.find_element_by_class_name('forum-title').text == 'Marcin'
    app.wd.find_element_by_xpath("//*[@title='Post a new topic']").click()
    app.wd.fid_element_by_id("subject").click()
    app.wd.fid_element_by_id("subject").send_keys("test1")
    time.sleep(2)

