from lib.fruit_repository import FruitRepository
from lib.fruit import Fruit

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/fruit_store.sql") # Seed our database with some test data
    repository = FruitRepository(db_connection) # Create a new BookRepository

    fruits = repository.all()

    # Assert on the results
    assert fruits == [
        Fruit(1, "Apple", 15),
        Fruit(2, "Pear", 1),
        Fruit(3, "Orange", 3),
        Fruit(4, "Mango", 8),
        Fruit(5, "Kiwi", 25)
    ]

def test_get_one_fruit_by_id(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/fruit_store.sql") # Seed our database with some test data
    repository = FruitRepository(db_connection) # Create a new BookRepository

    fruit = repository.find(3)

    # Assert on the results
    assert fruit == Fruit(3, "Orange", 3)

def test_create(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/fruit_store.sql") # Seed our database with some test data
    repository = FruitRepository(db_connection) # Create a new BookRepository
    
    fruit = Fruit(None, 'Strawberry', 23)
    new_fruit = repository.create(fruit)
    fruit.id = new_fruit.id
    assert new_fruit == fruit

def test_delete(db_connection):
    db_connection.seed("seeds/fruit_store.sql") # Seed our database with some test data
    repository = FruitRepository(db_connection)

    repository.delete(6)
    fruits = repository.all()

    assert fruits == [
        Fruit(1, "Apple", 15),
        Fruit(2, "Pear", 1),
        Fruit(3, "Orange", 3),
        Fruit(4, "Mango", 8),
        Fruit(5, "Kiwi", 25)
    ]