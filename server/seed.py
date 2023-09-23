from random import choice as rc
from faker import Faker
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

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

pizza_ingredients = [
    'Mozzarella Cheese', 'Tomato Sauce', 'Pepperoni', 'Mushrooms',
    'Sausage', 'Peppers', 'Black Olives', 'Bacon', 'Basil', 'Ham',
    'Parmesan Cheese', 'Red Peppers', 'Jalapeño Peppers', 'Onions', 'Garlic',
    'Anchovies', 'Spinach', 'Pineapple', 'Artichoke Hearts', 'Sun-Dried Tomatoes',
    'Provolone Cheese', 'Ricotta Cheese', 'Feta Cheese', 'Cheddar Cheese',
    'Capers', 'Pesto Sauce', 'Blue Cheese', 'Arugula'
]

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurants = []
    for i in range(20):
        restaurant = Restaurant(
            name = fake.unique.company(),
            address = fake.unique.address()[:14]
        )
        restaurants.append(restaurant)

    db.session.add_all(restaurants)

    pizza_name = rc(popular_pizza_names)

    pizzas = []
    for i in range(20):
        num_ingredients = rc([3, 4])
        selected_ingredients = [rc(pizza_ingredients)
                                for i in range(num_ingredients)]

        pizza = Pizza(
            name = rc(popular_pizza_names),
            ingredients = ", ".join(selected_ingredients)
        )
        pizzas.append(pizza)

    db.session.add_all(pizzas)

    restaurant_pizzas = []

    for i in range(20):
        restaurant_pizza = RestaurantPizza(
            pizza_id = rc(range(1, 21)),
            restaurant_id = rc(range(1, 21)),
            price = rc(range(1, 30))
        )
        restaurant_pizzas.append(restaurant_pizza)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()
