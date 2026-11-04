from math import gcd
import unittest


def _simplify(frac):
    """Funkcja pomocnicza: skraca ułamek i dba o to, by mianownik był dodatni."""
    num, den = frac
    if den == 0:
        raise ValueError("Mianownik nie może być zerem")

    common = gcd(num, den)
    num //= common
    den //= common

    # Znak minusa przenosimy zawsze do licznika
    if den < 0:
        num = -num
        den = -den

    return [num, den]


def add_frac(frac1, frac2):
    """Dodawanie ułamków: a/b + c/d = (a*d + c*b) / (b*d)"""
    num = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return _simplify([num, den])


def sub_frac(frac1, frac2):
    """Odejmowanie ułamków: a/b - c/d = (a*d - c*b) / (b*d)"""
    num = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    den = frac1[1] * frac2[1]
    return _simplify([num, den])


def mul_frac(frac1, frac2):
    """Mnożenie ułamków: (a/b) * (c/d) = (a*c) / (b*d)"""
    num = frac1[0] * frac2[0]
    den = frac1[1] * frac2[1]
    return _simplify([num, den])


def div_frac(frac1, frac2):
    """Dzielenie ułamków: (a/b) / (c/d) = (a*d) / (b*c)"""
    if frac2[0] == 0:
        raise ZeroDivisionError("Nie można dzielić przez ułamek o wartości zero")
    num = frac1[0] * frac2[1]
    den = frac1[1] * frac2[0]
    return _simplify([num, den])


def is_positive(frac):
    """Zwraca True, jeśli ułamek jest dodatni (> 0)."""
    # Iloczyn licznika i mianownika jest dodatni tylko wtedy, gdy oba mają ten sam znak
    return (frac[0] * frac[1]) > 0


def is_zero(frac):
    """Zwraca True, jeśli ułamek ma wartość 0."""
    return frac[0] == 0 and frac[1] != 0


def cmp_frac(frac1, frac2):
    """
    Porównuje dwa ułamki:
    zwraca -1 gdy frac1 < frac2,
             0 gdy frac1 == frac2,
            +1 gdy frac1 > frac2.
    """
    diff = sub_frac(frac1, frac2)
    if diff[0] == 0:
        return 0
    return 1 if diff[0] > 0 else -1


def frac2float(frac):
    """Konwertuje ułamek do postaci zmiennoprzecinkowej (float)."""
    return frac[0] / frac[1]


# ---------------------------------------------------------
# Testy jednostkowe
# ---------------------------------------------------------

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [1, 2]
        self.f2 = [1, 3]
        self.f3 = [-1, 2]
        self.f4 = [1, -2]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 4], [1, 4]), [1, 2])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 2], [1, 2]), [0, 1])
        self.assertEqual(sub_frac([1, 4], [3, 4]), [-1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [2, 3]), [1, 3])
        self.assertEqual(mul_frac([-1, 2], [2, 3]), [-1, 3])
        self.assertEqual(mul_frac([0, 1], [3, 5]), [0, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 2], [-1, 2]), [-1, 1])
        with self.assertRaises(ZeroDivisionError):
            div_frac([1, 2], [0, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([3, 4]))
        self.assertTrue(is_positive([-3, -4]))
        self.assertFalse(is_positive([-3, 4]))
        self.assertFalse(is_positive([3, -4]))
        self.assertFalse(is_positive([0, 5]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, 7]))
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-2, 3]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), 0)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([1, 3]), 0.3333333333333333)
        self.assertAlmostEqual(frac2float([-1, 4]), -0.25)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()