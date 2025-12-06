class Operation:
    def execute(self, a, b):
        raise NotImplementedError("Метод execute має бути перевизначений")


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            return "Помилка: ділення на нуль!"
        return a / b
