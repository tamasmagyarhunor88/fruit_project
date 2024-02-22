from lib.fruit import Fruit

class FruitRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM fruits')
        fruits = []

        for row in rows:
            fruit = Fruit(row['id'], row['name'], row['calory'])
            fruits.append(fruit)
        return fruits
    
    def find(self, fruit_id):
        rows = self._connection.execute('SELECT * FROM fruits WHERE id = %s', [fruit_id])

        row = rows[0]
        fruit = Fruit(row['id'], row['name'], row['calory'])
        return fruit
    
    def create(self, fruit):
        rows = self._connection.execute('INSERT INTO fruits(name, calory) VALUES (%s, %s) RETURNING id', [fruit.name, fruit.calory])
        fruit.id = rows[0]['id']
        return fruit
    
    def delete(self, fruit_id):
        self._connection.execute('DELETE FROM fruits WHERE id = %s', [fruit_id])
        return None
