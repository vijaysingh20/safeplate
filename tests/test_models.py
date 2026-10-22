import pytest
from pydantic import ValidationError
from safeplate.models import RestaurantRecord, InspectionRecord


def test_restaurant_trims_whitespaces():
    restaurant = RestaurantRecord(
        restaurant_id="RST-001",
        name=" Green Bowl ",
        city=" Gurugram ",
        address=" Sector 49 ",
        cuisine=" Indian "
    )

    assert restaurant.name == "Green Bowl"
    assert restaurant.city == "Gurugram"
    assert restaurant.address == "Sector 49"
    assert restaurant.cuisine == "Indian"


def test_restaurant_rejects_blank_name():
    with pytest.raises(ValidationError):
        RestaurantRecord(
            restaurant_id="RST-001",
            name=" ",
            city="Gurugram",
            address="Sector 49",
            cuisine="Indian",
        )


def test_inspection_score_92():
    inspection = InspectionRecord(
        inspection_id="INS-001",
        restaurant_id="RST-001",
        inspection_date="2025-12-10",
        score=92,
        critical_violations=0
    )


def test_inspection_score_0():
    inspection = InspectionRecord(
        inspection_id="INS-001",
        restaurant_id="RST-001",
        inspection_date="2025-12-10",
        score=0,
        critical_violations=0
    )


def test_inspection_score_100():
    inspection = InspectionRecord(
        inspection_id="INS-001",
        restaurant_id="RST-001",
        inspection_date="2025-12-10",
        score=100,
        critical_violations=0
    )


def test_inspection_rejects_score_above_100():
    with pytest.raises(ValidationError):
        InspectionRecord(
            inspection_id="INS-001",
            restaurant_id="RST-001",
            inspection_date="2025-12-10",
            score=101,
            critical_violations=0,
        )


def test_inspection_score_below_0():
    with pytest.raises(ValidationError):
        InspectionRecord(
            inspection_id="INS-001",
            restaurant_id="RST-001",
            inspection_date="2025-12-10",
            score=-1,
            critical_violations=0,
        )


def test_inspection_score_critical_violations():
    with pytest.raises(ValidationError):
        InspectionRecord(
            inspection_id="INS-001",
            restaurant_id="RST-001",
            inspection_date="2025-12-10",
            score=92,
            critical_violations=-1,
        )