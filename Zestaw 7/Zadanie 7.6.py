import random
import unittest

# (a) Zwracający 0, 1, 0, 1, 0, 1, ...
class ZeroOneIterator:
    def __iter__(self):
        return self

    def __next__(self):
        val = self._val
        self._val = 1 - self._val  # przełącza między 0 i 1
        return val

    def __init__(self):
        self._val = 0


# (b) Zwracający losowo jedną wartość z ("N", "E", "S", "W") 
class RandomWalkIterator:
    def __init__(self):
        self.directions = ("N", "E", "S", "W")

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.directions)


# (c) Zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [dni tygodnia]
class WeekdayIterator:
    def __init__(self):
        self._val = 0

    def __iter__(self):
        return self

    def __next__(self):
        val = self._val
        self._val = (self._val + 1) % 7
        return val


# Kod testujący moduł z asercjami
class TestIterators(unittest.TestCase):
    def test_zero_one_iterator(self):
        it = iter(ZeroOneIterator())
        expected = [0, 1, 0, 1, 0, 1]
        results = [next(it) for _ in range(6)]
        self.assertEqual(results, expected)

    def test_random_walk_iterator(self):
        it = iter(RandomWalkIterator())
        directions = {"N", "E", "S", "W"}
        for _ in range(20):
            val = next(it)
            self.assertIn(val, directions)

    def test_weekday_iterator(self):
        it = iter(WeekdayIterator())
        expected = [0, 1, 2, 3, 4, 5, 6, 0, 1]
        results = [next(it) for _ in range(9)]
        self.assertEqual(results, expected)

if __name__ == "__main__":
    unittest.main()