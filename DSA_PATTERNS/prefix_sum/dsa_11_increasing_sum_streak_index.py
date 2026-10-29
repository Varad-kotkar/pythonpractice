"""
Problem 11: Longest Increasing Running-Sum Streak with Starting Index

Return (longest_streak_length, starting_index).
Count increases, not elements.
If there are no increases, return (0, -1).
"""

def longest_increasing_sum_streak_index(numbers):
    # Step 1: Initialize variables
    running_sum=0
    previous_sum=0
    starting_index=0
    current_index=0
    current_streak=0
    longest_streak_length=0
    for index,num in enumerate(numbers):
        previous_sum=running_sum
        running_sum+=num
        if index==0:
            continue
        if running_sum>previous_sum:
            # current_index=index
            current_streak+=1
            if current_streak==1:
                current_index=index
        else:
            current_streak=0
            current_index=-1
        # if current_streak==1:
        #     current_index=index
        if current_streak>longest_streak_length:
            longest_streak_length=current_streak
            starting_index=current_index
    if longest_streak_length==0:
        return (0,-1)

    return longest_streak_length,starting_index


    # Step 2: Calculate running sums


    # Step 3: Compare each sum with the previous sum


    # Step 4: Track the current streak and its starting index


    # Step 5: Update the longest streak and its starting index


    # Step 6: Return the result
   


# Test cases
print(longest_increasing_sum_streak_index([3, 2, 4, 1, 5, 2]))  # Expected: (5, 1)
print(longest_increasing_sum_streak_index([1, 2, 3, 4]))        # Expected: (3, 1)
print(longest_increasing_sum_streak_index([5, -1, -1]))         # Expected: (0, -1)
print(longest_increasing_sum_streak_index([3, -3, 0, 2]))       # Expected: (1, 3)
print(longest_increasing_sum_streak_index([]))                  # Expected: (0, -1)