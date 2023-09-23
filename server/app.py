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
    def get(self):
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
    def get(self, num):
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
    def get(self):
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
    def post(self):
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
