import sqlite3
import pytest

from safeplate.db import get_connection, init_db


def test_init_db_creates_table(tmp_path):
    db_path = tmp_path / "safeplate.db"
    init_db(db_path)

    connection = get_connection(db_path)
    try:
        rows = connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall()

        table_names = {row["name"] for row in rows}
        assert {"restaurants", "inspections"} <= table_names
    finally:
        connection.close()


def test_inspection_rejects_unknown_restaurant(tmp_path):
    db_path = tmp_path / "safeplate.db"
    init_db(db_path)

    connection = get_connection(db_path)

    try:
        with pytest.raises(
            sqlite3.IntegrityError,
            match="FOREIGN KEY constraint failed"
        ):
            connection.execute(
                """
                INSERT INTO inspections (
                    inspection_id,
                    restaurant_id,
                    inspection_date,
                    score,
                    critical_violations
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                ("INS-001", "RST-999", "2026-10-20", 92, 0)
            )
    finally:
        connection.close()