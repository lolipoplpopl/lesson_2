"""
Unit tests for StringUtils class.
"""

import unittest
from string_utils import StringUtils


class TestStringUtils(unittest.TestCase):
    """
    Test cases for StringUtils class.
    """
    
    def setUp(self):
        """Set up test fixture."""
        self.utils = StringUtils()
    
    # Tests for capitilize
    def test_capitilize_positive(self):
        """Test capitilize with normal strings."""
        self.assertEqual(self.utils.capitilize("skypro"), "Skypro")
        self.assertEqual(self.utils.capitilize("hello"), "Hello")
        self.assertEqual(self.utils.capitilize("test"), "Test")
    
    def test_capitilize_empty(self):
        """Test capitilize with empty string."""
        self.assertEqual(self.utils.capitilize(""), "")
    
    def test_capitilize_already_capitalized(self):
        """Test capitilize with already capitalized string."""
        self.assertEqual(self.utils.capitilize("Already"), "Already")
    
    def test_capitilize_with_numbers(self):
        """Test capitilize with string starting with numbers."""
        self.assertEqual(self.utils.capitilize("123abc"), "123abc")
    
    # Tests for trim
    def test_trim_positive(self):
        """Test trim with leading spaces."""
        self.assertEqual(self.utils.trim("   skypro"), "skypro")
        self.assertEqual(self.utils.trim("  hello"), "hello")
        self.assertEqual(self.utils.trim(" world"), "world")
    
    def test_trim_empty(self):
        """Test trim with empty string."""
        self.assertEqual(self.utils.trim(""), "")
    
    def test_trim_no_spaces(self):
        """Test trim with string without leading spaces."""
        self.assertEqual(self.utils.trim("skypro"), "skypro")
    
    def test_trim_multiple_spaces(self):
        """Test trim with multiple leading spaces."""
        self.assertEqual(self.utils.trim("     test"), "test")
    
    def test_trim_only_spaces(self):
        """Test trim with string containing only spaces."""
        self.assertEqual(self.utils.trim("    "), "")
    
    # Tests for to_list
    def test_to_list_default_delimiter(self):
        """Test to_list with default delimiter."""
        self.assertEqual(self.utils.to_list("a,b,c"), ["a", "b", "c"])
        self.assertEqual(self.utils.to_list("1,2,3,4"), ["1", "2", "3", "4"])
    
    def test_to_list_custom_delimiter(self):
        """Test to_list with custom delimiter."""
        self.assertEqual(self.utils.to_list("a;b;c", ";"), ["a", "b", "c"])
        self.assertEqual(self.utils.to_list("1-2-3", "-"), ["1", "2", "3"])
    
    def test_to_list_empty(self):
        """Test to_list with empty string."""
        self.assertEqual(self.utils.to_list(""), [])
    
    def test_to_list_single_element(self):
        """Test to_list with single element."""
        self.assertEqual(self.utils.to_list("a"), ["a"])
    
    def test_to_list_with_spaces(self):
        """Test to_list with spaces around delimiter."""
        self.assertEqual(self.utils.to_list("a, b, c"), ["a", " b", " c"])
    
    # Tests for contains
    def test_contains_positive(self):
        """Test contains with existing symbols."""
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertTrue(self.utils.contains("SkyPro", "k"))
        self.assertTrue(self.utils.contains("SkyPro", "o"))
    
    def test_contains_negative(self):
        """Test contains with non-existing symbols."""
        self.assertFalse(self.utils.contains("SkyPro", "X"))
        self.assertFalse(self.utils.contains("", "a"))
    
    def test_contains_case_sensitive(self):
        """Test contains case sensitivity."""
        self.assertTrue(self.utils.contains("SkyPro", "S"))
        self.assertFalse(self.utils.contains("SkyPro", "s"))  # Defect!
    
    # Tests for delete_symbol
    def test_delete_symbol_positive(self):
        """Test delete_symbol with existing symbols."""
        self.assertEqual(self.utils.delete_symbol("SkyPro", "k"), "SyPro")
        self.assertEqual(self.utils.delete_symbol("hello", "l"), "helo")
    
    def test_delete_symbol_not_found(self):
        """Test delete_symbol with non-existing symbol."""
        self.assertEqual(self.utils.delete_symbol("SkyPro", "x"), "SkyPro")
    
    def test_delete_symbol_multiple_occurrences(self):
        """Test delete_symbol with multiple occurrences."""
        self.assertEqual(self.utils.delete_symbol("hello", "l"), "helo")  # Defect!
    
    def test_delete_symbol_empty_string(self):
        """Test delete_symbol with empty string."""
        self.assertEqual(self.utils.delete_symbol("", "a"), "")
    
    # Tests for starts_with
    def test_starts_with_positive(self):
        """Test starts_with with matching symbols."""
        self.assertTrue(self.utils.starts_with("SkyPro", "S"))
        self.assertTrue(self.utils.starts_with("123abc", "1"))
    
    def test_starts_with_negative(self):
        """Test starts_with with non-matching symbols."""
        self.assertFalse(self.utils.starts_with("SkyPro", "s"))  # Defect!
        self.assertFalse(self.utils.starts_with("SkyPro", "P"))
    
    def test_starts_with_empty_string(self):
        """Test starts_with with empty string."""
        self.assertFalse(self.utils.starts_with("", "a"))
    
    # Tests for end_with
    def test_end_with_positive(self):
        """Test end_with with matching symbols."""
        self.assertTrue(self.utils.end_with("SkyPro", "o"))
        self.assertTrue(self.utils.end_with("123abc", "c"))
    
    def test_end_with_negative(self):
        """Test end_with with non-matching symbols."""
        self.assertFalse(self.utils.end_with("SkyPro", "O"))  # Defect!
        self.assertFalse(self.utils.end_with("SkyPro", "S"))
    
    def test_end_with_empty_string(self):
        """Test end_with with empty string."""
        self.assertFalse(self.utils.end_with("", "a"))
    
    # Tests for is_empty
    def test_is_empty_positive(self):
        """Test is_empty with empty string."""
        self.assertTrue(self.utils.is_empty(""))
    
    def test_is_empty_negative(self):
        """Test is_empty with non-empty strings."""
        self.assertFalse(self.utils.is_empty("SkyPro"))
        self.assertFalse(self.utils.is_empty(" "))  # Defect!
        self.assertFalse(self.utils.is_empty("  "))  # Defect!
    
    def test_is_empty_with_spaces(self):
        """Test is_empty with spaces-only string."""
        self.assertFalse(self.utils.is_empty("   "))  # Defect!
    
    # Tests for list_to_string
    def test_list_to_string_default(self):
        """Test list_to_string with default joiner."""
        self.assertEqual(self.utils.list_to_string(["a", "b", "c"]), "a, b, c")
        self.assertEqual(self.utils.list_to_string(["1", "2", "3"]), "1, 2, 3")
    
    def test_list_to_string_custom_joiner(self):
        """Test list_to_string with custom joiner."""
        self.assertEqual(self.utils.list_to_string(["a", "b", "c"], "-"), "a-b-c")
        self.assertEqual(self.utils.list_to_string(["a", "b", "c"], ""), "abc")
    
    def test_list_to_string_single_element(self):
        """Test list_to_string with single element list."""
        self.assertEqual(self.utils.list_to_string(["a"]), "a")
    
    def test_list_to_string_empty_list(self):
        """Test list_to_string with empty list."""
        # This test should fail due to defect
        with self.assertRaises(Exception):
            self.utils.list_to_string([])


if __name__ == '__main__':
    unittest.main()