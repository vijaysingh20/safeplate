from safeplate.models import RestaurantRecord
from itertools import product


def build_restaurants() -> list[RestaurantRecord]:
    restaurants = list()
    names = [
        "Green Bowl",
        "Copper Spoon",
        "Maple Kitchen",
        "Saffron Courtyard",
        "Willow Table"
    ]

    cities = [
        "Gurugram",
        "Delhi",
        "Jaipur",
        "Pune",
        "Bengaluru"
    ]

    for i, (name, city) in enumerate(product(names, cities), start=1):
        restaurant = RestaurantRecord(
            restaurant_id=f"RST-{i:03d}",
            name=name,
            city=city,
            address=f"{name}, {city}",
            cuisine="Indian"
        )
        restaurants.append(restaurant)
    return restaurants