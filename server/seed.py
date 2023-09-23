"""
This script generates random data for restaurants, pizzas,
and restaurant-pizza associations
using the Faker library and adds them to a database.
"""

from random import choice as rc
from faker import Faker

from app import app

from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

# List of popular pizza names
popular_pizza_names = [
    "Margherita",
    "Pepperoni",
    "Supreme",
    "Hawaiian",
    "Vegetarian",
    "Meat Lovers",
    "BBQ Chicken",
    "Mushroom",
    "Sausage",
    "White Pizza",
    "Buffalo Chicken",
    "Pesto",
    "Four Cheese",
    "Veggie Delight",
    "Spinach and Feta",
    "Bacon Ranch",
    "Chicken Alfredo",
    "Capricciosa",
    "Taco Pizza",
    "Seafood",
]

# List of pizza ingredients
pizza_ingredients = [
    'Mozzarella Cheese', 'Tomato Sauce', 'Pepperoni', 'Mushrooms',
    'Sausage', 'Peppers', 'Black Olives', 'Bacon', 'Basil', 'Ham',
    'Parmesan Cheese', 'Red Peppers', 'Jalapeño Peppers', 'Onions', 'Garlic',
    'Anchovies', 'Spinach', 'Pineapple', 'Artichoke Hearts', 'Sun-Dried Tomatoes',
    'Provolone Cheese', 'Ricotta Cheese', 'Feta Cheese', 'Cheddar Cheese',
    'Capers', 'Pesto Sauce', 'Blue Cheese', 'Arugula'
]

with app.app_context():

    # Clear existing data
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Generate random restaurants
    restaurants = []

    for i in range(20):
        restaurant = Restaurant(
            name=fake.unique.company()[:50],  # Limit name to 50 characters
            # Limit address to 14 characters
            address=fake.unique.address()[:14]
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)

    # Generate random pizzas
    pizza_name = rc(popular_pizza_names)

    pizzas = []
    for i in range(20):
        num_ingredients = rc([3, 4])
        selected_ingredients = [rc(pizza_ingredients)
                                for i in range(num_ingredients)]

        pizza = Pizza(
            name=rc(popular_pizza_names),
            ingredients=", ".join(selected_ingredients)
        )
        pizzas.append(pizza)

    db.session.add_all(pizzas)

    # Generate random restaurant_pizzas
    restaurant_pizzas = []

    for i in range(20):
        restaurant_pizza = RestaurantPizza(
            pizza_id=rc(range(1, 21)),
            restaurant_id=rc(range(1, 21)),
            price=rc(range(1, 30))
        )
        restaurant_pizzas.append(restaurant_pizza)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()
