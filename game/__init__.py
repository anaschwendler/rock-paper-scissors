import os
import random

from flask import Flask, flash, redirect, render_template, request, url_for

from . import db
from game.db import get_db
from game.helper import GAME_OPTIONS, GAME_TYPES, define_winner, define_winner_name
from game.queries import (
    fetch_last_session,
    finalize_session,
    save_player_names,
    update_scores,
)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "game.sqlite"),
    )

    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        print(test_config)
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def index():
        """First screen to allow the player to select a game mode"""
        # TODO: move this to model function
        last_session = fetch_last_session()

        return render_template("index.html", last_session=last_session)

    @app.route("/new_round", methods=("GET", "POST"))
    def new_round():
        """Start new round/game, request player names"""
        if request.method == "POST":
            game_type = request.form["game-type"]

            if game_type not in GAME_TYPES:
                flash("Invalid game type")
                return redirect(url_for("index"))
        else:
            flash("Invalid action")
            return redirect(url_for("index"))

        return render_template("game/new_round.html", game_type=game_type)

    @app.route("/round", methods=("GET", "POST"))
    def round():
        """From new round/game, request player moves"""
        random_move = ""

        if request.method == "POST":
            player_one = request.form["player-one"]
            player_two = request.form["player-two"]

            if player_two == "Computer":
                random_move = random.choice(list(GAME_OPTIONS.values()))

            save_player_names(player_one, player_two)

        elif request.method == "GET":
            database = get_db()

            last_session = fetch_last_session()

            if last_session["session_completed"]:
                flash("Session is finished")
                return redirect(url_for("index"))
            else:
                if last_session["player_two_name"] == "Computer":
                    random_move = random.choice(list(GAME_OPTIONS.values()))

        return render_template(
            "game/player_move.html", game_options=GAME_OPTIONS, random_move=random_move
        )

    @app.route("/round_result", methods=("GET", "POST"))
    def round_result():
        """From new round/game, shows round results"""
        if request.method == "POST":
            player_one_move = request.form["player-one-move"]
            player_two_move = request.form["player-two-move"]

            if (
                player_one_move not in GAME_OPTIONS.values()
                or player_two_move not in GAME_OPTIONS.values()
            ):
                flash("Invalid move!")
                return redirect(url_for("index"))

            result_hash = define_winner(player_one_move, player_two_move)

            update_scores(result_hash["winner"])

            last_session = fetch_last_session()

            winner_name = define_winner_name(result_hash["winner"])

            result_hash = {
                "winner": winner_name,
                "text": result_hash["result_text"],
                "player_one_name": last_session["player_one_name"],
                "player_two_name": last_session["player_two_name"],
                "player_one_score": last_session["player_one_score"],
                "player_two_score": last_session["player_two_score"],
            }
            return render_template("game/round_result.html", result_hash=result_hash)
        else:
            flash("Invalid action")
            return redirect(url_for("index"))

    @app.route("/finish_session")
    def finish_session():
        """Finalizes session"""
        finalize_session()
        return render_template("game/finish_session.html")

    @app.errorhandler(404)
    def page_not_found(e):
        """In case a non-existing page is requested, returns 404"""
        return render_template("404.html")

    return app
