import unittest

from utils import get_data
from custom_sort import sort_entries


class TestCustomSort(unittest.TestCase):
    """Test custom_sort.py solution."""

    def setUp(self):
        """Set up data for tests."""
        self.entries_data = get_data('entries.txt')
        self.result_data = get_data('result.txt')

    def test_custom_sort_sample(self):
        """Test custom_sort function with sample data."""
        criteria_data = get_data('criteria.txt')
        result = sort_entries(self.entries_data, criteria_data)
        self.assertEqual(result, self.result_data)

    def test_custom_sort_criteria(self):
        """Test custom_sort with custom criteria."""
        criteria_data = [
            ('width', '>=', 2),
            ('length', '<=', 20),
        ]
        result = sort_entries(self.entries_data, criteria_data)
        self.assertNotEqual(result, self.entries_data)


if __name__ == '__main__':
    unittest.main()
