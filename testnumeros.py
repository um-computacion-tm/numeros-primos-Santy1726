from primos import is_primo
import unittest

def is_primo(value):
    div = 2
    if value == 1:
        return False
    while div < value:
        if value % div == 0:
            return False
        div +=1
    return True






class TestsPrimos (unittest.TestCase):
    def test_1(Self):
        result = is_primo(1)
        Self.assertEqual(result, False) 

    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)

    def test_7(self):
        result = is_primo(7)
        self.assertEqual(result, True)

    def test_11(self):
        result = is_primo(11)
        self.assertEqual(result, True)
    
    def test_12(self):
        result = is_primo(12)
        self.assertEqual(result, False)

unittest.main()

        




