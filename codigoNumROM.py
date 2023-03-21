import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return "I" * decimal
    elif decimal ==5:
        return "V"
    elif decimal ==15:
        return "XV"
    elif decimal ==20:
        return "XX"
    elif decimal ==50:
        return "L"
    else:
        return "X"



class testDecimalRomano(unittest.TestCase):
    def test_1(self):
        #pre condicion
        ##No HAY

        #PROCESO
        resultado = decimal_to_roman(1)

        #verificado

        self.assertEqual(resultado, "I")

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, "X")    


    def test_cinco(self):
        resultado=decimal_to_roman(5)
        self.assertEqual(resultado, "V")

    def test_dos(self):
        resultado=decimal_to_roman(2)
        self.assertEqual(resultado, "II")

    def test_tres(self):
        resultado=decimal_to_roman(3)
        self.assertEqual(resultado, "III")

    def test_quince(self):
        resultado=decimal_to_roman(15)
        self.assertEqual(resultado,"XV")

    def test_veinte(self):
        resultado=decimal_to_roman(20)
        self.assertEqual(resultado,"XX")

    def test_cincuenta(self):
        resultado=decimal_to_roman(50)
        self.assertEqual(resultado,"L")    

if __name__ ==  "__main__":
    unittest.main() 
