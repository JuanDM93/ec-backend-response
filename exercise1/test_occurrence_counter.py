"""
Test ocurrence_counter.py solution.

Usage:
    python test_ocurrence_counter.py
"""
import unittest

from utils import get_data_from_file
from occurrence_counter import count_word


class TestOcurrenceCounter(unittest.TestCase):
    """Test ocurrence_count.py solution."""

    def setUp(self):
        """Set up data for tests."""
        self.file_data = get_data_from_file('text.txt')

    def test_count_word_success(self):
        """Test count_word function."""
        word = 'logística'
        count = count_word(self.file_data, word)
        self.assertEqual(count, 4)
        self.assertNotEqual(count, 0)

    def test_count_word_fail(self):
        """Test count_word function."""
        word = 'logistica'
        count = count_word(self.file_data, word)
        self.assertEqual(count, 0)
        self.assertNotEqual(count, 4)


if __name__ == '__main__':
    unittest.main()
