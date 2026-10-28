# Problem 14: Valid Palindrome
# Pattern: Two Pointers
# Difficulty: Easy

def is_palindrome(text):
    # Initialize your pointers
    left=0
    right=len(text)-1
    while left<right:
        if text[left]==text[right]:
            left+=1
            right-=1
        else:
            return False
    return True
    # Compare characters while the pointers have not met or crossed

        # Decide what to do if the characters differ

        # Decide what to do if the characters match

    # Return the final result


# Tests
print(is_palindrome("madam"))   # Expected: True
print(is_palindrome("python"))  # Expected: False
print(is_palindrome("abba"))    # Expected: True
print(is_palindrome("a"))       # Expected: True
print(is_palindrome(""))        # Expected: True