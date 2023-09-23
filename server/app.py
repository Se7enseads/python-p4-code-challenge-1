"""
This Flask application is designed for managing restaurants and pizzas.

Database Models:
    The application uses the following SQLAlchemy database models:

    - `Restaurant`: Represents restaurant information, including name and address.
    - `Pizza`: Represents pizza information, including name and ingredients.
    - `RestaurantPizza`: Represents the association between restaurants and pizzas,
                         including the price.
"""

from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)


class Restaurants(Resource):
    """
    Resource for retrieving restaurant data.

    Provides endpoints for listing all restaurants.
    """

    def get(self):
        """
        Get a list of all restaurants.

        Returns:
            List[dict]: A list of restaurant data.
        """

        pizzas = Restaurant.query.all()

        restaurants_data = []
        for restaurant in pizzas:
            restaurant_data = {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
            restaurants_data.append(restaurant_data)

        return restaurants_data


api.add_resource(Restaurants, '/restaurants')


class RestaurantByID(Resource):
    """
    Resource for retrieving and deleting restaurant data by ID.

    Provides endpoints for getting restaurant details and deleting a restaurant.
    """

    def get(self, num):
        """
        Get details of a restaurant by ID.

        Args:
            num (int): The ID of the restaurant to retrieve.

        Returns:
            dict: Restaurant details including associated pizzas.
        """

        restaurant = Restaurant.query.filter(Restaurant.id == num).first()

        if restaurant:
            restaurant_body = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": [
                    {
                        "id": restaurant_pizza.pizza.id,
                        "name": restaurant_pizza.pizza.name,
                        "ingredients": restaurant_pizza.pizza.ingredients
                    }
                    for restaurant_pizza in restaurant.restaurant_pizzas
                ]
            }

            return restaurant_body

        return {
            "error": "Restaurant not found"
        }, 404

    def delete(self, num):
        """
        Delete a restaurant by ID.

        Args:
            num (int): The ID of the restaurant to delete.

        Returns:
            dict: Empty response.
        """

        restaurant = Restaurant.query.filter(Restaurant.id == num).first()
        restaurant_pizza = RestaurantPizza.query.filter(
            RestaurantPizza.restaurant_id == num).first()

        if not restaurant:
            return {
                "error": "Restaurant not found"
            }, 404

        if restaurant_pizza:
            db.session.delete(restaurant_pizza)

        db.session.delete(restaurant)
        db.session.commit()

        return {}, 200


api.add_resource(RestaurantByID, '/restaurants/<int:num>')


class Pizzas(Resource):
    """
    Resource for retrieving pizza data.

    Provides an endpoint for listing all pizzas.
    """

    def get(self):
        """
        Get a list of all pizzas.

        Returns:
            List[dict]: A list of pizza data.
        """

        pizzas = Pizza.query.all()

        pizzas_data = []
        for pizza in pizzas:
            restaurant_data = {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.ingredients
            }
            pizzas_data.append(restaurant_data)

        return pizzas_data


api.add_resource(Pizzas, '/pizzas')


class RestaurantPizzas(Resource):
    """
    Resource for creating restaurant pizzas.

    Provides an endpoint for creating restaurant pizza entries.
    """

    def post(self):
        """
        Create a new restaurant pizza entry.

        Returns:
            dict: Restaurant pizza details.
        """

        data = request.get_json()

        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])

        if not pizza or not restaurant:
            return {
                "errors": ["Pizza or Restaurant not found"]
            }, 404

        new_restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )

        db.session.add(new_restaurant_pizza)
        db.session.commit()

        response_body = {
            "id": new_restaurant_pizza.pizza.id,
            "name": new_restaurant_pizza.pizza.name,
            "ingredients": new_restaurant_pizza.pizza.ingredients
        }

        return response_body, 201


api.add_resource(RestaurantPizzas, '/restaurant_pizzas')


if __name__ == '__main__':
    app.run(port=5555, debug=True)
