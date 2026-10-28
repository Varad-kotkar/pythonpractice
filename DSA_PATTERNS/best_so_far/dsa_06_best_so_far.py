
"""
DSA Pattern: Best-So-Far
Problem 6: Second-Highest Distinct Score

Return the second-highest distinct integer.
Return None if it does not exist.

Requirements:
- Do not use max() or sorting.
- Traverse the list once.
- Track highest and second_highest.
- Handle duplicates and negative numbers.
"""

def second_highest_score(scores):
    highest=None
    # sec_highest=None

    for i in scores:
        if highest is None or i > highest:
            sec_highest=highest
            highest=i
    sec_highest=None
    for i in scores:
        if i == highest:
            continue
        if sec_highest is None or i> sec_highest :
            sec_highest=i
        
    return sec_highest
    
#optmized

def second_highest_score(scores):
    highest = None
    sec_highest = None

    for i in scores:
        if highest is None or i > highest:
            # if i != highest:
            sec_highest = highest
            highest = i
        elif i != highest and (
            sec_highest is None or i > sec_highest
        ):
            sec_highest = i

    return sec_highest


# TEST CASES
print(second_highest_score([12, 5, 18, 9, 14]))  # Expected: 14
print(second_highest_score([7, 7, 4]))           # Expected: 4
print(second_highest_score([5, 5, 5]))           # Expected: None
print(second_highest_score([-8, -3, -10]))       # Expected: -8
print(second_highest_score([4, 9]))              # Expected: 4
print(second_highest_score([]))                  # Expected: None
print(second_highest_score([3, 8, 8, 6]))        # Expected: 6
