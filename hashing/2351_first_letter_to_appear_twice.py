"""
2351. First Letter to Appear Twice

Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

- A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
- s will contain at least one letter that appears twice.
"""


def repeated_character(s: str) -> str:
    # We use a set because the second ocurrence
    # just need to be seen one time.
    existing_chars = set()
    for char in s:
        if char in existing_chars:
            return char
        existing_chars.add(char)
    return ''


if __name__ == "__main__":
    assert(repeated_character('abccbaacz') == 'c')
    assert(repeated_character('abcdd') == 'd')
