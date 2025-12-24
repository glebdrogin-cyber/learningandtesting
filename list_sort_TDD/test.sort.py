import unittest
from typing import List

def unique_sorted(numbers: List[int]) -> List[int]:
    # Entfernt Duplikate aus einer Liste ganzer Zahlen und gibt
    # eine aufsteigend sortierte neue Liste zurück.

    # Args:
    #   numbers (List[int]): Eine Liste ganzer Zahlen.

    # Returns:
    #    List[int]: Sortierte Liste ohne Duplikate.
    # set entfernt Duplikate, sorted sorgt für aufsteigende Reihenfolge
    return sorted(set(numbers))

class TestUniqueSorted(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(unique_sorted([]), [])

    def test_single_element(self):
        self.assertEqual(unique_sorted([5]), [5])

    def test_list_with_duplicates(self):
        self.assertEqual(unique_sorted([3, 1, 2, 3, 2, 1]), [1, 2, 3])

    def test_already_sorted_list(self):
        self.assertEqual(unique_sorted([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_unsorted_list(self):
        self.assertEqual(unique_sorted([4, 2, 1, 3]), [1, 2, 3, 4])

    def test_negative_numbers(self):
        self.assertEqual(unique_sorted([0, -1, -1, 2]), [-1, 0, 2])


if __name__ == "__main__":
    unittest.main()