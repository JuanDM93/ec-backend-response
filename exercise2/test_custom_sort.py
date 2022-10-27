import unittest

from utils import get_data_from_file
from custom_sort import sort_entries


class TestCustomSort(unittest.TestCase):
    """Test custom_sort.py solution."""

    entries_data = eval(get_data_from_file('entries.txt'))
    result_data = eval(get_data_from_file('result.txt'))

    def test_custom_sort_sample(self):
        """Test custom_sort function with sample data."""
        criteria_data = get_data_from_file('criteria.txt')
        criteria_data = eval(criteria_data)
        result = sort_entries(self.entries_data, criteria_data)
        self.assertEqual(result, self.result_data)


if __name__ == '__main__':
    unittest.main()
