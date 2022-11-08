"""
2351. First Letter to Appear Twice

Given a string s consisting of lowercase English letters,
return the first letter to appear twice.

Note:

- A letter a appears twice before another letter b if the
second occurrence of a is before the second occurrence of b.
- s will contain at least one letter that appears twice.
"""


def repeated_char(s: str) -> str:
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return ''


if __name__ == '__main__':
    assert(repeated_char("abccbaacz") == "c")
    assert(repeated_char("abcdd") == "d")
