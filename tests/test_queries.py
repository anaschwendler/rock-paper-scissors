from game.db import get_db
from game.queries import (
    fetch_last_session,
    finalize_session,
    save_player_names,
    update_scores,
)


def test_fetch_last_session(app):
    with app.app_context():
        result = fetch_last_session()
        assert result["player_one_name"] == "foo"


def test_finalize_session(app):
    with app.app_context():
        finalize_session()
        result = fetch_last_session()
        assert result["session_completed"] == True


def test_save_player_names(app):
    with app.app_context():
        save_player_names("Jane", "Doe")
        result = fetch_last_session()
        assert result["player_one_name"] == "Jane"
        assert result["player_two_name"] == "Doe"


def test_update_scores(app):
    with app.app_context():
        update_scores(1)
        result = fetch_last_session()
        assert result["player_one_score"] == 1
