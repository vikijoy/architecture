class Employee:
    name: str

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"