class Fruit():
    def __init__(self, id, name, calory) -> None:
        self.id = id
        self.name = name
        self.calory = calory

    def __repr__(self):
        return f"Fruit({self.id}, {self.name}, {self.calory})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__