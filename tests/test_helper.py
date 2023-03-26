from game.helper import define_winner, define_winner_name


def test_define_winner_name(app):
    with app.app_context():
        winner_name = define_winner_name(2)
        assert winner_name == "bar"


def test_define_winner():
    result = define_winner("R", "S")
    expected_hash = {"result_text": "Rock smashes scissors!", "winner": 1}
    assert result == expected_hash
