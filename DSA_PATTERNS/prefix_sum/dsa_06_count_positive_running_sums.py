
"""
Problem 6: Count Positive Running Sums

Count how many times the running sum becomes greater than zero
after processing each change.
"""

def count_positive_running_sums(changes):
    # Step 1: Initialize your variables
    running_sum=0
    count=0
    for i in changes:
        running_sum+=i
        if running_sum>0:
            count+=1
    return count

    # Step 2: Process each change


    # Step 3: Check whether the running sum is positive


    # Step 4: Return the count
    

# Test cases
print(count_positive_running_sums([2, -1, -3, 4]))  # Expected: 2
print(count_positive_running_sums([-2, 3, -1, 2]))  # Expected: 3
print(count_positive_running_sums([-1, -2, -3]))    # Expected: 0
print(count_positive_running_sums([1, 1, 1]))       # Expected: 3
print(count_positive_running_sums([]))              # Expected: 0
