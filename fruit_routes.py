from lib.database_connection import get_flask_database_connection
from lib.fruit_repository import FruitRepository
from lib.fruit import Fruit
from flask import request, render_template, redirect, url_for

# You won't need to nest your routes in app.py in a method like this
def apply_fruit_routes(app):
    # GET /fruits
    # Returns a list of fruits
    @app.route('/fruits', methods=['GET'])
    def get_fruits():
        connection = get_flask_database_connection(app)
        repository = FruitRepository(connection)
        fruits = repository.all()
        return render_template('fruits/index.html', fruits=fruits)
    
    @app.route('/fruits/<int:id>', methods=['GET'])
    def get_fruit(id):
        connection = get_flask_database_connection(app)
        repository = FruitRepository(connection)
        fruit = repository.find(id)
        return render_template('fruits/show.html', fruit=fruit)
    
    @app.route('/fruits/new', methods=['GET'])
    def new_fruit_form():
        return render_template('fruits/new.html')
    
    @app.route('/fruits', methods=['POST'])
    def create_fruit():
        name = request.form['name']
        calory = request.form['calory']
        fruit = Fruit(None, name, calory)

        connection = get_flask_database_connection(app)
        repository = FruitRepository(connection)
        created_fruit = repository.create(fruit)
        fruit_id = created_fruit.id

        return redirect(f"/fruits/{fruit_id}")
