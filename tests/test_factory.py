from game import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_index(client):
    response = client.get("/")
    assert len(response.data) > 0
    assert response.status == "200 OK"
