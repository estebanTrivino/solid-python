# Incorrecto

class Form:

    def draw_square(self):
        print("Dibujar un cuadrado")

    def draw_circle(self):
        print("Dibujar un circulo")

# Correcto

class Form:
    def draw(self):
        # Permite dibujar una forma

class Square(Form):
    def draw(self):
        print("Dibuja un cuadrado")

class Circle(Form):
    def draw(self):
        print("Dibuja un circulo")

class Triangle(Form):
    def draw(self):
        print("Dibuja un triangulo")


# Extra - Calculadora

from abc import ABC, abstractmethod


class Operation(ABC):
    @abstractmethod
    def execute(self,a,b):
        pass

class Addition(Operation):
    def execute(self,a,b):
        return a + b

class Substraction(Operation):
    def execute(self,a,b):
        return a - b

class Multiplication(Operation):
    def execute(self,a,b):
        return a * b

class Division(Operation):
    def execute(self,a,b):
        return a / b

class Calculator: 
    def __init__(self) -> None:
        self.operations = {}

    def add_operation(self, name, operation):
        self.operation[name] = operation

    def calculate(self, name, a, b):
        if name not in self.operation:
            rais ValueError(f"La operacion {name} no está soportada.")
        return self.operations[name].execute(a, b)

calculator = Calculator()
calculator.add_operation("Addition", Addition())
calculator.add_operation("Substraction", Substraction())
calculator.add_operation("Multiplication", Multiplication())
calculator.add_operation("Division", Division())

print(calculator.calculate("Addition", 10, 2))