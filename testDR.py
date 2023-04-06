
import unittest
from codigoNumROM import decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decimal_to_roman(1), "I")

    def test_2(self):
        self.assertEqual(decimal_to_roman(2), "II")

    def test_3(self):
        self.assertEqual(decimal_to_roman(3), "III")

    def test_4(self):
        self.assertEqual(decimal_to_roman(4), "IV")

    def test_5(self):
        self.assertEqual(decimal_to_roman(5), "V")

    def test_9(self):
        self.assertEqual(decimal_to_roman(9), "IX")

    def test_10(self):
        self.assertEqual(decimal_to_roman(10), "X")

    def test_11(self):
        self.assertEqual(decimal_to_roman(11), "XI")

    def test_14(self):
        self.assertEqual(decimal_to_roman(14), "XIV")

    def test_15(self):
        self.assertEqual(decimal_to_roman(15), "XV")

    def test_19(self):
        self.assertEqual(decimal_to_roman(19), "XIX")

    def test_20(self):
        self.assertEqual(decimal_to_roman(20), "XX")

    def test_40(self):
        self.assertEqual(decimal_to_roman(40), "XL")

    def test_50(self):
        self.assertEqual(decimal_to_roman(50), "L")

    def test_90(self):
        self.assertEqual(decimal_to_roman(90), "XC")

    def test_100(self):
        self.assertEqual(decimal_to_roman(100), "C")

    def test_400(self):
        self.assertEqual(decimal_to_roman(400), "CD")

    def test_500(self):
        self.assertEqual(decimal_to_roman(500), "D")

    def test_900(self):
        self.assertEqual(decimal_to_roman(900), "CM")

    def test_1000(self):
        self.assertEqual(decimal_to_roman(1000), "M")

if __name__ == '__main__':

    unittest.main()
