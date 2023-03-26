from game.queries import fetch_last_session

GAME_OPTIONS = {"ROCK": "R", "PAPER": "P", "SCISSORS": "S"}
GAME_TYPES = {"versus", "computer", "continue"}


def define_winner_name(winner):
    """Define round winner.

    :param winner: represent winner code (0: tie, 1: player_one, 2: player_two)
    :return: the winner name of the round
    """

    last_session = fetch_last_session()

    if winner == 1:
        winner_name = last_session["player_one_name"]
    elif winner == 2:
        winner_name = last_session["player_two_name"]
    else:
        winner_name = "No one"

    return winner_name


def define_winner(player_one_move, player_two_move):
    """Define round winner.

    :param player_one_move: represent player one move
    :param player_two_move: represent player two move
    :return: the winner/result of the round
    """

    result = {"result_text": "", "winner": 0}

    if player_one_move == player_two_move:
        result["result_text"] = "It's a tie!"
    elif player_one_move == "R":
        if player_two_move == "S":
            result["result_text"] = "Rock smashes scissors!"
            result["winner"] = 1
        else:
            result["result_text"] = "Paper covers rock!"
            result["winner"] = 2
    elif player_one_move == "P":
        if player_two_move == "R":
            result["result_text"] = "Paper covers rock!"
            result["winner"] = 1
        else:
            result["result_text"] = "Scissors cuts paper!"
            result["winner"] = 2
    elif player_one_move == "S":
        if player_two_move == "P":
            result["result_text"] = "Scissors cuts paper!"
            result["winner"] = 1
        else:
            result["result_text"] = "Rock smashes scissors!"
            result["winner"] = 2

    return result
