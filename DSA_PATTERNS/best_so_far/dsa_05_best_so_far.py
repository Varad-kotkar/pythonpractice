
"""
DSA Pattern: Best-So-Far
Problem 5: Find the Highest Score

Return the highest integer in the list.
Return None if the list is empty.

Requirements:
- Do not use max().
- Traverse the list once.
- Track the best score found so far.

Expected examples:
[12, 5, 18, 9, 14] -> 18
[-8, -3, -10]      -> -3
[7]                -> 7
[]                 -> None
[4, 4, 4]          -> 4
"""

def highest_score(scores):
    highest=None
    for score in scores:
        if highest is None or score>highest:
            highest=score
    return highest
    


# TEST CASES
print(highest_score([12, 5, 18, 9, 14]))  # Expected: 18
print(highest_score([-8, -3, -10]))        # Expected: -3
print(highest_score([7]))                  # Expected: 7
print(highest_score([]))                   # Expected: None
print(highest_score([4, 4, 4]))            # Expected: 4
print(highest_score([-5, -2, -9, -1]))     # Expected: -1
