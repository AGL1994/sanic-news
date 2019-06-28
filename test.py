# from servers.server import app
from server import app


def test_t():
    request, response = app.test_client.post('/user')
    assert response.status == 200


test_t()