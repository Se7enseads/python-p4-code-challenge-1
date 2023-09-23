"""
Database Models:
    The application uses the following SQLAlchemy database models:

    - `Restaurant`: Represents restaurant information, including name and address.
    - `Pizza`: Represents pizza information, including name and ingredients.
    - `RestaurantPizza`: Represents the association between restaurants and pizzas,
                         including the price.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model):
    """
    Database model representing a restaurant.

    Attributes:
        - id (int): The primary key for the restaurant.
        - name (str): The name of the restaurant (unique).
        - address (str): The address of the restaurant.

        - restaurant_pizzas (Relationship): One-to-many relationship with RestaurantPizza.
    """

    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    @validates('name')
    def name_validation(self, key, res_name):
        """
        Validate the name of the restaurant.

        Args:
            key (str): The name of the attribute being validated ('name').
            name (str): The name value to be validated.

        Raises:
            ValueError: If the name is not unique or exceeds 50 characters in length.
        """

        names = db.session.query(Restaurant.name).all()

        if res_name in names:
            raise ValueError('Name must be unique')

        if len(res_name) > 50:
            raise ValueError('Name must less than 50 characters in length')

        return res_name

    def __repr__ (self):
        return f'<Restaurant: Name: {self.name} Address: {self.address}>'

class Pizza(db.Model):
    """
    Database model representing a pizza.

    Attributes:
        - id (int): The primary key for the pizza.
        - name (str): The name of the pizza.
        - ingredients (str): The ingredients of the pizza.
        - created_at (DateTime): The creation timestamp for the pizza.
        - updated_at (DateTime): The update timestamp for the pizza.
        
        - restaurant_pizzas (Relationship): One-to-many relationship with RestaurantPizza.
    """

    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    def __repr__ (self):
        return f'<Pizza: Name: {self.name} Ingredients: {self.ingredients}>'

class RestaurantPizza(db.Model):
    """
    Database model representing a restaurant-pizza association.

    Attributes:
        - id (int): The primary key for the restaurant-pizza association.
        - pizza_id (int): The foreign key reference to the pizza.
        - restaurant_id (int): The foreign key reference to the restaurant.
        - price (int): The price of the pizza at the restaurant.
        - created_at (DateTime): The creation timestamp for the association.
        - updated_at (DateTime): The update timestamp for the association.
        
        - pizza (Relationship): Many-to-one relationship with Pizza.
        - restaurant (Relationship): Many-to-one relationship with Restaurant.
    """

    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')

    @validates('price')
    def price_validation(self, key, rp_price):
        """
        Validate the price of the restaurant pizza.

        Args:
            key (str): The name of the attribute being validated ('price').
            price (int): The price value to be validated.

        Raises:
            ValueError: If the price is not within the range [1, 30].
        """

        if rp_price not in range(1, 31):
            raise ValueError('Price must be between 1 and 30')
        return rp_price

    def __repr__ (self):
        return (
            f'<RestaurantPizza: Pizza_id: {self.pizza_id}' 
            f'Restaurant_id: {self.restaurant_id} Price: {self.price}>'
        )
