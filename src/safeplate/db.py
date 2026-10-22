import sqlite3
from pathlib import Path


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL CHECK(length(trim(name)) > 0),
    city TEXT NOT NULL CHECK(length(trim(city)) > 0),
    address TEXT NOT NULL CHECK(length(trim(address)) > 0),
    cuisine TEXT NOT NULL CHECK(length(trim(cuisine)) > 0)
);

CREATE TABLE IF NOT EXISTS inspections (
    inspection_id TEXT PRIMARY KEY NOT NULL,
    restaurant_id TEXT NOT NULL REFERENCES restaurants(restaurant_id),
    inspection_date TEXT NOT NULL,
    score INTEGER NOT NULL CHECK(score BETWEEN 0 AND 100),
    critical_violations INTEGER NOT NULL CHECK(critical_violations >= 0)
);
"""


def get_connection(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(db_path)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection


def init_db(db_path: Path) -> None:
    connection = get_connection(db_path)
    try:
        connection.executescript(SCHEMA_SQL)
    finally:
        connection.close()