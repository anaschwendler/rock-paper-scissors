from game.db import get_db


def fetch_last_session():
    """Fetch last session information"""

    return (
        get_db().execute("SELECT * FROM session ORDER BY id DESC LIMIT 1;").fetchone()
    )


def finalize_session():
    """Finalize last session"""
    last_session = fetch_last_session()

    if not last_session["session_completed"]:
        session_id = last_session["id"]

        database = get_db()
        database.execute(
            "UPDATE session SET session_completed = ?" " WHERE id = ?", (1, session_id)
        )
        database.commit()


def save_player_names(player_one, player_two):
    """Save player names

    :param player_one: represent player one name
    :param player_two: represent player two name
    """
    database = get_db()
    database.execute(
        "INSERT INTO session (player_one_name, player_two_name) VALUES (?, ?)",
        (player_one, player_two),
    )
    database.commit()


def update_scores(winner):
    """Save player names

    :param winner: represent winner fo the round
    """
    last_session = fetch_last_session()

    session_id = last_session["id"]

    player_one_score = 1 if winner == 1 else 0
    player_two_score = 1 if winner == 2 else 0

    player_one_new_score = last_session["player_one_score"] + player_one_score
    player_two_new_score = last_session["player_two_score"] + player_two_score

    database = get_db()

    database.execute(
        "UPDATE session SET player_one_score = ?, player_two_score = ?" " WHERE id = ?",
        (player_one_new_score, player_two_new_score, session_id),
    )
    database.commit()
