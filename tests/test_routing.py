def test_index(client):
    response = client.get("/")
    assert response.status == "200 OK"
    assert b"Rock, paper, scissor game!" in response.data


def test_new_round_sucess(client):
    response = client.post("/new_round", data={"game-type": "versus"})
    assert response.status == "200 OK"
    assert b"Versus mode" in response.data


def test_new_round_invalid_game_type(client):
    response = client.post("/new_round", data={"game-type": "foo"})
    assert response.status == "302 FOUND"  # redirect


def test_round_sucess(client):
    response = client.post("/round", data={"player-one": "foo", "player-two": "bar"})
    assert response.status == "200 OK"
    assert b"Make your move!" in response.data


def test_round_against_computer(client):
    response = client.post(
        "/round", data={"player-one": "foo", "player-two": "Computer"}
    )
    assert response.status == "200 OK"
    assert b"Playing against computer" in response.data


def test_round_result_sucess(client):
    response = client.post(
        "/round_result", data={"player-one-move": "R", "player-two-move": "S"}
    )
    assert response.status == "200 OK"
    assert b"Rock smashes scissors!" in response.data


def test_round_result_invalid_move(client):
    response = client.post(
        "/round_result", data={"player-one-move": "X", "player-two-move": "S"}
    )
    assert response.status == "302 FOUND"  # redirect


def test_finish_session_sucess(client):
    response = client.get("/finish_session")
    assert response.status == "200 OK"
    assert b"Thanks for playing!" in response.data
