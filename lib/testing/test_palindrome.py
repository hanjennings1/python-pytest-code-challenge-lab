import pytest
from palindrome import longest_palindromic_substring


class TestLongestPalindromicSubstring:

    # --- Basic Cases ---
    def test_papaya_returns_valid_palindrome(self):
        result = longest_palindromic_substring("papaya")
        assert result in ("pap", "apa", "aya")

    def test_cbbd_returns_bb(self):
        assert longest_palindromic_substring("cbbd") == "bb"

    def test_full_string_is_palindrome(self):
        assert longest_palindromic_substring("hannah") == "hannah"


    # --- Edge Cases ---
    def test_single_character_string(self):
        assert longest_palindromic_substring("a") == "a"

    def test_two_different_characters(self):
        assert longest_palindromic_substring("az") in ("a", "z")

    def test_empty_string_returns_empty_string(self):
        assert longest_palindromic_substring("") == ""

    def test_all_identical_characters(self):
        assert longest_palindromic_substring("hhhhh") == "hhhhh"

    def test_no_palindrome_longer_than_one_character(self):
        result = longest_palindromic_substring("abcde")
        assert len(result) == 1
        assert result in "abcde"

    def test_palindrome_in_middle_of_string(self):
        result = longest_palindromic_substring("kayaking")
        assert result == "kayak"

    def test_mixed_case_letters(self):
        result = longest_palindromic_substring("Aa")
        assert result in ("A", "a")

    def test_numeric_characters(self):
        assert longest_palindromic_substring("12321") == "12321"      # numeric, but a string because of the quotes

    def test_long_string_near_max_length(self):
        input_string = "a" * 1000
        result = longest_palindromic_substring(input_string)
        assert result == input_string
        assert len(result) == 1000


    # --- Failure Cases ---
    def test_none_input_raises_type_error(self):
        with pytest.raises(TypeError):
            longest_palindromic_substring(None)

    def test_integer_input_raises_type_error(self):
        with pytest.raises(TypeError):
            longest_palindromic_substring(12321)      # numeric - NOT a string

    def test_list_input_raises_type_error(self):
        with pytest.raises(TypeError):
            longest_palindromic_substring(["a", "b", "a"])