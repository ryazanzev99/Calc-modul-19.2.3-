
from app.new_calc import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_cor(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_cor(self):
        assert self.calc.division(self, 15, 3) == 5

    def test_subtraction_cor(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding_cor(self):
        assert self.calc.adding(self, 4, 7) == 11


