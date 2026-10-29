"""
Problem 10: Longest Streak of Increasing Running Sums

Find the longest consecutive streak of strictly increasing
running sums. Count increases, not elements.
"""

def longest_increasing_sum_streak(numbers):
    # Step 1: Initialize your variables
    running_sum=0
    previous_sum=0
    longest_streak=0
    current_streak=0
    # for num in range(len(numbers)) :
    for index, num in enumerate(numbers):
        previous_sum = running_sum
        running_sum += num
        # running_sum+=num
        # # if index>0:
        # previous_sum=running_sum-num
#imp step 
        if index>0:
            if running_sum >previous_sum          :
                current_streak+=1

            else:
                current_streak=0

    # Step 4: Update the current streak and longest streak
        if current_streak>longest_streak:
            longest_streak=current_streak

    # Step 5: Return the longest streak
    return longest_streak


# Test cases
print(longest_increasing_sum_streak([2, 3, -1, 4, -6, 2]))  # Expected: 1
print(longest_increasing_sum_streak([1, 2, 3, 4]))          # Expected: 3
print(longest_increasing_sum_streak([5, -1, -1, -1]))       # Expected: 1
print(longest_increasing_sum_streak([3, -3, 0, 2]))         # Expected: 2
print(longest_increasing_sum_streak([-2, -3, -4]))          # Expected: 0
print(longest_increasing_sum_streak([]))                    # Expected: 0