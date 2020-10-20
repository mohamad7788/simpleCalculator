import unittest

from calculator import Calculator


class Tests(unittest.TestCase):
    def setUp(self):
        self._caclulator = Calculator()

    def test_prefix_missing_not_a_number(self):
      self.assertRaises(Exception, self._caclulator.calculate, '+ 1 a')

    def test_prefix_missing_arg(self):
      self.assertRaises(Exception, self._caclulator.calculate, '+ 1')

    def test_prefix_none(self):
      self.assertRaises(Exception, self._caclulator.calculate, '')

    def test_prefix_1_plus_1(self):
        result = self._caclulator.calculate('+ 1 1')
        assert result == 2

    def test_prefix_2_plus_3(self):
        result = self._caclulator.calculate('+ 2 3')
        assert result == 5

    def test_prefix_1_plus_2_plus_3(self):
        result = self._caclulator.calculate('+ 1 2 3')
        assert result == 6
      
    def test_prefix_1_mult_2_mult_3(self):
        result = self._caclulator.calculate('* 1 2 3')
        assert result == 6
    
    def test_prefix_1_plus_10_plus_200(self):
        result = self._caclulator.calculate('+ 1 10 200')
        assert result == 211
    
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    unittest.TextTestRunner().run(suite)

    # calculator = Calculator()
    # print(calculator.calculate('+ 1 1'))
