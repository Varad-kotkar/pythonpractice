
"""
Problem 8: Longest Positive Streak with Starting Index

Find the longest consecutive streak during which the running
sum remains strictly positive.

Return (longest_length, starting_index).
If no positive streak exists, return (-1, 0).
If multiple streaks have equal maximum length, choose the first.
"""

def longest_positive_streak_index(changes):
    # Step 1: Initialize the running sum and streak variables
    running_sum=0
    longest=0
    count=0
    starting_index=0
    current_start=0

    for i in range(len(changes)):
        running_sum+=changes[i]
        if running_sum>0:
            # starting_index=i
            count+=1

#imp step
            if count==1:
                current_start=i

        else:
            count=0
        if longest<count:
            longest=count
#imp step
            starting_index=current_start
    if longest==0:
        return (-1,0)
    return longest,starting_index

    # Step 2: Process each change while tracking its index


    # Step 3: Track the current positive streak and its start


    # Step 4: Update the best streak and its starting index


    # Step 5: Return the result
    pass


# Test cases — expected outputs verified by manual tracing
print(longest_positive_streak_index([2, -1, -3, 4, 2, -1]))
# Expected: (3, 3)

print(longest_positive_streak_index([1, 1, -5, 2, 2]))
# Expected: (2, 0)

print(longest_positive_streak_index([-1, -2, -3]))
# Expected: (-1, 0)

print(longest_positive_streak_index([1, 1, 1]))
# Expected: (3, 0)

print(longest_positive_streak_index([]))
# Expected: (-1, 0)

print(longest_positive_streak_index([2, -2, 1, -1, 3]))
# Expected: (2, 2)
