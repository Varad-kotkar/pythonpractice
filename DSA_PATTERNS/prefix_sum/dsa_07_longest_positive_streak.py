"""**Filename:** `dsa_07_longest_positive_streak.py`

**Difficulty:** Easy → Medium  
**Pattern:** Running Sum + Streak Tracking

**Problem statement**

Given a list of integers representing balance changes, calculate the running sum from left to right.

Return the length of the longest consecutive sequence of steps where the running sum is strictly greater than zero.

If the running sum is zero or negative, the current positive streak ends.

Return `0` if no running sum is positive.

**Examples**

```python
print(longest_positive_streak([2, -1, -3, 4, 2, -1]))  # Expected: 3
print(longest_positive_streak([-2, -1, 3, 1]))         # Expected: 2
print(longest_positive_streak([1, 1, 1, 1]))           # Expected: 4
print(longest_positive_streak([-1, -2, -3]))           # Expected: 0
print(longest_positive_streak([]))                     # Expected: 0
```

**Copy this complete starter file into your editor:**"""

"""
Problem 7: Longest Positive Balance Streak

Find the longest consecutive streak during which the running
sum remains strictly greater than zero.
"""

def longest_positive_streak(changes):
    # Step 1: Initialize the required variables
    running_sum=0
    longest=0
    count=0
    for i in changes:
        running_sum+=i
        if running_sum>0:
            count+=1
            # if longest<count:
            #     longest=count
        else:
            count=0
        if longest<count:
            longest=count
    return longest

    # Step 2: Process each change and update the running sum


    # Step 3: Track the current positive streak


    # Step 4: Update the longest streak when necessary


    # Step 5: Return the longest streak
    pass


# Test cases
print(longest_positive_streak([2, -1, -3, 4, 2, -1]))  # Expected: 3
print(longest_positive_streak([-2, -1, 3, 1]))         # Expected: 2
print(longest_positive_streak([1, 1, 1, 1]))            # Expected: 4
print(longest_positive_streak([-1, -2, -3]))            # Expected: 0
print(longest_positive_streak([]))                      # Expected: 0
