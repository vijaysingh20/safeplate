from pathlib import Path

from safeplate.db import get_connection
from safeplate.models import RestaurantRecord, InspectionRecord


def insert_restaurant(
    db_path: Path,
    restaurant: RestaurantRecord
) -> None:
    connection = get_connection(db_path)
    try:
        query = """
            INSERT INTO restaurants (
                restaurant_id,
                name,
                city,
                address,
                cuisine
            )
            VALUES (?, ?, ?, ?, ?)
        """
        values = (
            restaurant.restaurant_id,
            restaurant.name,
            restaurant.city,
            restaurant.address,
            restaurant.cuisine
        )

        connection.execute(query, values)
        connection.commit()
    finally:
        connection.close()


def insert_inspection(
    db_path: Path,
    inspection: InspectionRecord,
) -> None:
    connection = get_connection(db_path)
    try:
        query = """
            INSERT INTO inspections(
                inspection_id,
                restaurant_id,
                inspection_date,
                score,
                critical_violations
            )
            VALUES (?, ?, ?, ?, ?)
        """
        values = (
            inspection.inspection_id,
            inspection.restaurant_id,
            inspection.inspection_date.isoformat(),
            inspection.score,
            inspection.critical_violations
        )
        connection.execute(query, values)
        connection.commit()
    finally:
        connection.close()