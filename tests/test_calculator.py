import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_multiplay_calculate_correcty(self):
        assert self.calc.multiply(self, 5, 4) == 20

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 3) == 5

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 8, 3) == 11