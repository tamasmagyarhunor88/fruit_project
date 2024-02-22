from lib.fruit import Fruit

def test_fruit_constructs():
    fruit = Fruit(1, "Apple", 15)
    assert fruit.id == 1
    assert fruit.name == "Apple"
    assert fruit.calory == 15

def test_fruit_format_nicely():
    fruit = Fruit(1, "Apple", 15)
    assert str(fruit) == "Fruit(1, Apple, 15)"

def test_fruits_are_equal():
    fruit = Fruit(1, "Apple", 15)
    fruit2 = Fruit(1, "Apple", 15)
    assert fruit == fruit2