def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """

    if not isinstance(s, str):
        raise TypeError("Input must be a string")  # guard clause for bad input types


    if len(s) < 2:
        return s  # empty string or single char is trivially its own longest palindrome


    start = 0
    max_length = 1

    def expand_around_center(left, right):
        # grow outward while both sides match and stay in bounds
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # loop overshoots by 1 on each side, so subtract back

    for i in range(len(s)):
        odd_length = expand_around_center(i, i)      # odd-length palindrome centered on i
        even_length = expand_around_center(i, i + 1)  # even-length palindrome centered between i, i+1

        current_max = max(odd_length, even_length)
        if current_max > max_length:
            max_length = current_max
            start = i - (current_max - 1) // 2  # recompute start index for the new longest match


    return s[start:start + max_length]