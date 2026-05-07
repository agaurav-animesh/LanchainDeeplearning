
class Calculator:
    def add(self, x, y):
        return x + y

calc = Calculator()
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", calc.add(a, b))