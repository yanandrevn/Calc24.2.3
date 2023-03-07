import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_successful(self):
       assert self.calc.adding(self, 2, 2) == 4

    def test_subtraction_successful(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_multiply_successful(self):
        assert self.calc.multiply(self, 5, 5) == 25

    def test_division_successful(self):
        assert self.calc.division(self, 8, 4) == 2


