DROP TABLE IF EXISTS session;

CREATE TABLE session (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  player_one_name TEXT CHECK( LENGTH(player_one_name) <= 20 ) NOT NULL DEFAULT '',
  player_two_name TEXT CHECK( LENGTH(player_two_name) <= 20 ) NOT NULL DEFAULT '',
  player_one_score INTEGER NOT NULL DEFAULT 0,
  player_two_score INTEGER NOT NULL DEFAULT 0,
  session_completed INTEGER CHECK( session_completed IN (0,1) ) DEFAULT 0
);