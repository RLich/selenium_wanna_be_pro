import pytest
from application import Application
from Config.cfg_att import Config
import time


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def subforum_number():
    subforum_link = "a[href$='viewforum.php?f=4"

def test_enter_subforum(app):
    app.login(username=Config.username, password=Config.password)
    app.nav_to_subforum()
    time.sleep(3)