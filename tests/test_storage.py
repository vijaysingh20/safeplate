from safeplate.db import get_connection, init_db
from safeplate.models import RestaurantRecord, InspectionRecord
from safeplate.storage import insert_restaurant, insert_inspection


def test_insert_restaurant_persists(tmp_path):
    db_path = tmp_path / "safeplate.db"
    init_db(db_path)

    restaurant = RestaurantRecord(
        restaurant_id="RST-001",
        name="Chef's Table",
        city="Gurugram",
        address="Sector 49",
        cuisine="Indian"
    )

    insert_restaurant(db_path, restaurant)
    connection = get_connection(db_path)

    try:
        row = connection.execute(
            "SELECT * FROM restaurants WHERE restaurant_id = ?",
            (restaurant.restaurant_id,),
        ).fetchone()

        assert row is not None
        assert dict(row) == restaurant.model_dump()
    finally:
        connection.close()


def test_insert_inspection_persists(tmp_path):
    db_path = tmp_path / "safeplate.db"
    init_db(db_path)

    restaurant = RestaurantRecord(
        restaurant_id="RST-001",
        name="Green Bowl",
        city="Gurugram",
        address="Sector 49",
        cuisine="Indian",
    )
    insert_restaurant(db_path, restaurant)

    inspection = InspectionRecord(
        inspection_id="INS-001",
        restaurant_id="RST-001",
        inspection_date="2026-10-20",
        score=92,
        critical_violations=0
    )

    insert_inspection(db_path, inspection)
    connection = get_connection(db_path)

    try:
        row = connection.execute(
            "SELECT * FROM inspections WHERE inspection_id = ?",
            ("INS-001",),
        ).fetchone()
        assert row is not None
        assert row["restaurant_id"] == "RST-001"
        assert row["inspection_date"] == "2026-10-20"
        assert row["score"] == 92
        assert row["critical_violations"] == 0
    finally:
        connection.close()