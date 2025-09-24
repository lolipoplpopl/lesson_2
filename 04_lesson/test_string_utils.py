import pytest
from string_utils import StringUtils


class TestStringUtils:
    utils = StringUtils()

    # Тесты для capitalize
    def test_capitalize_positive(self):
        assert self.utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty(self):
        assert self.utils.capitalize("") == ""

    def test_capitalize_with_spaces(self):
        assert self.utils.capitalize(" hello") == " hello"

    def test_capitalize_mixed_case(self):
        assert self.utils.capitalize("sKYPRO") == "Skypro"

    # Тесты для trim
    def test_trim_positive(self):
        assert self.utils.trim("   hello") == "hello"

    def test_trim_empty(self):
        assert self.utils.trim("") == ""

    def test_trim_no_spaces(self):
        assert self.utils.trim("hello") == "hello"

    def test_trim_multiple_spaces(self):
        assert self.utils.trim("     hello") == "hello"

    def test_trim_spaces_in_middle(self):
        assert self.utils.trim("hello   world") == "hello   world"

    # Тесты для contains
    def test_contains_positive(self):
        assert self.utils.contains("SkyPro", "S") is True

    def test_contains_negative(self):
        assert self.utils.contains("SkyPro", "U") is False

    def test_contains_empty_string(self):
        assert self.utils.contains("", "a") is False

    def test_contains_empty_symbol(self):
        assert self.utils.contains("SkyPro", "") is True

    def test_contains_case_sensitive(self):
        assert self.utils.contains("SkyPro", "s") is False

    # Тесты для delete_symbol
    def test_delete_symbol_positive(self):
        assert self.utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert self.utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_nonexistent(self):
        assert self.utils.delete_symbol("SkyPro", "X") == "SkyPro"

    def test_delete_symbol_empty_string(self):
        assert self.utils.delete_symbol("", "a") == ""

    def test_delete_symbol_empty_symbol(self):
        assert self.utils.delete_symbol("SkyPro", "") == "SkyPro"

    def test_delete_symbol_all_occurrences(self):
        assert self.utils.delete_symbol("hello hello", "l") == "heo heo"

    # Негативные тесты с None
    def test_capitalize_none(self):
        with pytest.raises(AttributeError):
            self.utils.capitalize(None)

    def test_trim_none(self):
        with pytest.raises(AttributeError):
            self.utils.trim(None)

    def test_contains_none_string(self):
        with pytest.raises(AttributeError):
            self.utils.contains(None, "a")

    def test_contains_none_symbol(self):
        with pytest.raises(AttributeError):
            self.utils.contains("SkyPro", None)

    def test_delete_symbol_none_string(self):
        with pytest.raises(AttributeError):
            self.utils.delete_symbol(None, "a")

    def test_delete_symbol_none_symbol(self):
        with pytest.raises(AttributeError):
            self.utils.delete_symbol("SkyPro", None)
