from abc import ABC, abstractmethod


class Number(ABC):
    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def subtract(self, other):
        pass

    @abstractmethod
    def multiply(self, other):
        pass

    @abstractmethod
    def divide(self, other):
        pass

    @abstractmethod
    def display(self):
        pass


class Integer(Number):
    def __init__(self, value):
        self.value = int(value)

    def add(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        else:
            raise ValueError("Invalid type for addition")

    def subtract(self, other):
        if isinstance(other, Integer):
            return Integer(self.value - other.value)
        else:
            raise ValueError("Invalid type for subtraction")

    def multiply(self, other):
        if isinstance(other, Integer):
            return Integer(self.value * other.value)
        else:
            raise ValueError("Invalid type for multiplication")

    def divide(self, other):
        if isinstance(other, Integer) and other.value != 0:
            return Integer(self.value // other.value)
        else:
            raise ValueError("Invalid type or division by zero")

    def display(self):
        print(f"Integer Value: {self.value}")


class Real(Number):
    def __init__(self, value):
        self.value = float(value)

    def add(self, other):
        if isinstance(other, Real):
            return Real(self.value + other.value)
        else:
            raise ValueError("Invalid type for addition")

    def subtract(self, other):
        if isinstance(other, Real):
            return Real(self.value - other.value)
        else:
            raise ValueError("Invalid type for subtraction")

    def multiply(self, other):
        if isinstance(other, Real):
            return Real(self.value * other.value)
        else:
            raise ValueError("Invalid type for multiplication")

    def divide(self, other):
        if isinstance(other, Real) and other.value != 0:
            return Real(self.value / other.value)
        else:
            raise ValueError("Invalid type or division by zero")

    def display(self):
        print(f"Real Value: {self.value}")


def virtual_call_demo(number_obj):
    number_obj.display()


if __name__ == "__main__":
    integer1 = Integer(5)
    integer2 = Integer(3)

    real1 = Real(7.5)
    real2 = Real(2.5)

    # Demonstrating arithmetic operations
    result_add = integer1.add(integer2)
    result_add.display()

    result_subtract = real1.subtract(real2)
    result_subtract.display()

    result_multiply = integer1.multiply(integer2)
    result_multiply.display()

    result_divide = real1.divide(real2)
    result_divide.display()

    # Demonstrating virtual call
    virtual_call_demo(integer1)
    virtual_call_demo(real1)
