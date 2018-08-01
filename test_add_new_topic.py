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
    app.create_new_topic(topic_title, topic_text="teścik")
    assert app.get_name_of_topic_title(topic_title) == topic_title
    app.topic_cleanup(topic_title)


"""

def random_string(prefix, max_len):
symbols = string.ascii_letters + string.digits + " "
#  + string.punctuation to not fail tests as we know that it is not working correctly with this chars
return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])

"""