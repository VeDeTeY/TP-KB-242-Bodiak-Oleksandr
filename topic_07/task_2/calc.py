from operations import Add, Subtract, Multiply, Divide

class Calculator:
    def calculate(self, a, b, operation):
        if operation == "+":
            return Add().execute(a, b)
        elif operation == "-":
            return Subtract().execute(a, b)
        elif operation == "*":
            return Multiply().execute(a, b)
        elif operation == "/":
            return Divide().execute(a, b)
        else:
            return "Невідома операція!"
