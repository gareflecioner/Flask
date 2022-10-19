CREATE TABLE IF NOT EXISTS mainmenu (
    id       INTEGER PRIMARY KEY
                     UNIQUE
                     NOT NULL,
    title     TEXT    NOT NULL,
    url    TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS register (
    id       INTEGER PRIMARY KEY
                     UNIQUE
                     NOT NULL,
    name     TEXT    NOT NULL,
    email    TEXT    NOT NULL,
    password TEXT    NOT NULL,
    datatime INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS feedd (
    id       INTEGER PRIMARY KEY
                     UNIQUE
                     NOT NULL,
    name     TEXT    NOT NULL,
    text     TEXT    NOT NULL,
    datatime INTEGER NOT NULL
);
