
"""
Problem 5: First Target Position

Return the index where the running sum first equals the target.
Return -1 if the target is never reached.
"""

def first_target_position(changes, target):
    # Step 1: Initialize the running sum
    running_sum=0
    index={}
    for i in range(len(changes)):
        running_sum+=changes[i]
        if running_sum==target:
            return i
    return -1




        # if i not in index:
        #     index[i]=running_sum
        # if target==running_sum:
        #     return index[i]

    


    # Step 2: Process each change while tracking its index


    # Step 3: If the target is reached, return the index


    # Step 4: If the loop finishes without finding the target
    


# Test cases
print(first_target_position([2, 3, -1], 5))      # Expected: 1
print(first_target_position([3, -1, -2, 4], 0))   # Expected: 2
print(first_target_position([1, 2, 3], 10))       # Expected: -1
print(first_target_position([2, -2, 5], 0))       # Expected: 1
print(first_target_position([], 0))               # Expected: -1
