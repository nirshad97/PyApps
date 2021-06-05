from temp import Temperature


class Calorie:

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        try:
            result = 10 * self.weight + 6.5 * self.height + 5 - self.temperature * 10
            return result
        except TypeError:
            return self.temperature



