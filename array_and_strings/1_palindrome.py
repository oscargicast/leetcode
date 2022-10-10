"""
Example 1: Return true if a given string is a palindrome, false otherwise.

A string is a palindrome if it reads the same forwards as backwards.
That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".
"""

def is_palindrome(word):
    left_index = 0
    right_index = len(word) - 1
    while left_index < right_index:
        if word[left_index] != word[right_index]:
            return False
        left_index += 1
        right_index -= 1
    return True


if __name__ == "__main__":
    assert(is_palindrome('racecar') == True)
    assert(is_palindrome('anitalavalatina') == True)
    assert(is_palindrome('oscar') == False)
