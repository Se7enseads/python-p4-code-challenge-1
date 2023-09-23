from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model):

    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    @validates('name')
    def name_validation(self, key, name):
        names = db.session.query(Restaurant.name).all()

        if name in names:
            raise ValueError('Name must be unique')

        if len(name) > 50:
            raise ValueError('Name must less than 50 characters in length')

        return name

    def __repr__ (self):
        return f'<Restaurant: Name: {self.name} Address: {self.address}>'

class Pizza(db.Model):

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
    def price_validation(self, key, price):
        if price not in range(1, 31):
            raise ValueError('Price must be between 1 and 30')
        return price

    def __repr__ (self):
        return (
            f'<RestaurantPizza: Pizza_id: {self.pizza_id}' 
            f'Restaurant_id: {self.restaurant_id} Price: {self.price}>'
        )
