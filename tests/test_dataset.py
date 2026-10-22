from collections import Counter
from safeplate.generate.dataset import build_restaurants


def test_build_restaurants():
    restaurants = build_restaurants()

    assert len(restaurants) == 25
    assert len({r.restaurant_id for r in restaurants}) == 25

    name_counts = Counter(r.name for r in restaurants)
    assert len(name_counts) == 5
    assert all(count == 5 for count in name_counts.values())

    assert restaurants == build_restaurants()