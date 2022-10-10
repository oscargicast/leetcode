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
