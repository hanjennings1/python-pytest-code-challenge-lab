# Longest Palindromic Substring — Pytest Test Suite

A completed Test-Driven Development (TDD) exercise: a `pytest` test suite and working
implementation for finding the longest palindromic substring within a given string.

## Overview

This project follows a TDD workflow — the test suite was written first, confirmed to fail
against a stub implementation, and only then was the actual function implemented until all
tests passed.

**Function signature:**

```python
def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
```

**Constraints:**
- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters

## Project Structure

```
.
├── lib/
│   ├── palindrome.py              # Function implementation
│   └── testing/
│       └── test_palindrome.py     # Pytest test suite
├── pytest.ini                     # Pytest config (root directory)
├── Pipfile
└── README.md
```

## Setup

```bash
pipenv install
pipenv shell
pipenv install pytest
```

## Running the Tests

```bash
pytest
```

All 15 tests pass against the current implementation.

## Test Suite Coverage

The suite covers three categories, per TDD best practices:

### Basic Cases
- Multiple valid palindromes in one string (`"papaya"`)
- Single clear longest palindrome (`"cbbd"` → `"bb"`)
- Entire string is a palindrome (`"hannah"`)

### Edge Cases
- Single-character string
- Two different (non-palindromic) characters
- Empty string
- All identical characters
- No palindrome longer than one character
- Palindrome embedded mid-string, not centered or at the edges (`"kayaking"` → `"kayak"`)
- Mixed-case letters (case-sensitive comparison)
- Numeric characters as valid input
- Long string near the 1000-character upper bound

### Failure Cases
- `None` input → raises `TypeError`
- Integer input → raises `TypeError`
- List input → raises `TypeError`

## Implementation Notes

The function uses an **expand-around-center** approach:

- For each index in the string, treat it as a potential center of a palindrome and expand
  outward in both directions while characters match.
- Two expansions are checked per index — one for odd-length palindromes (single center) and
  one for even-length palindromes (double center) — to catch both patterns.
- Runs in O(n²) time, appropriate for the 1000-character constraint.
- Includes an explicit `isinstance(s, str)` type check at the top, so non-string input raises
  a clear, intentional `TypeError` rather than failing unpredictably (or silently succeeding,
  as would happen with a list).

```python
def longest_palindromic_substring(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    if len(s) < 2:
        return s

    start = 0
    max_length = 1

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        odd_length = expand_around_center(i, i)
        even_length = expand_around_center(i, i + 1)

        current_max = max(odd_length, even_length)
        if current_max > max_length:
            max_length = current_max
            start = i - (current_max - 1) // 2

    return s[start:start + max_length]
```

## TDD Verification

To confirm the test suite was genuinely tied to the implementation (not passing by
coincidence), the solution was temporarily reverted to a stub (`pass`) and the suite was
re-run — all 15 tests failed as expected. The real implementation was then restored, and all
tests passed again.

## What I Learned

- Writing tests *before* implementation clarifies expected behavior and catches ambiguous
  requirements early (e.g., inputs like `"papaya"` and `"babad"` have multiple valid correct
  answers, which changes how the assertions need to be written — membership checks instead
  of strict equality).
- A reference/"break glass" solution isn't automatically compatible with every reasonable
  test — the provided solution didn't include type validation, so certain failure-case tests
  required adding an explicit guard clause.
- Test configuration matters: an incorrectly placed `pytest.ini` (nested inside `lib/`
  instead of the project root) caused `ModuleNotFoundError`, since `pythonpath` is resolved
  relative to the config file's own location.