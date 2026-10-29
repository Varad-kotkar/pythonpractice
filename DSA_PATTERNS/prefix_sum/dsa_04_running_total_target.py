"""
Problem 4: Running Total Target

Count how many times the running balance equals the target.
Check the balance only after processing each change.
"""


def count_target_reaches(changes, target):
    # Step 1: Initialize your variables here
    running_sum=0
    count=0
    for i in changes:
        running_sum+=i
        if running_sum==target:
            count+=1
    return count


    # Step 2: Process the changes one by one


    # Step 3: Return the final count


# Test cases
print(count_target_reaches([2, 3, -1, 1], 5))  # Expected: 1
print(count_target_reaches([1, 2, -1, 2], 2))  # Expected: 1
print(count_target_reaches([2, -2, 2, -2], 0))  # Expected: 2
print(count_target_reaches([1, 2, -3], 0))     # Expected: 0
print(count_target_reaches([], 0))             # Expected: 0
