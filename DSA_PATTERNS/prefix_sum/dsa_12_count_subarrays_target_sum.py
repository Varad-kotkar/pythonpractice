"""
Problem 12: Count Subarrays with a Target Sum

Count the contiguous, non-empty subarrays whose sum equals target.
"""

def count_subarrays_target_sum(numbers, target):
    current_sum=0
    prefix_sum={0:1}
    count=0
    for index in range(len(numbers)):
        current_sum+=numbers[index]
        if current_sum-target in prefix_sum:
# imp to understand that adding 1 is not  correct bcz it give how many time appeard or matching found not only for 1 time  Instead, you need to add the number of times that required total appeared.
            count+=prefix_sum[current_sum-target]
# also important  dont use key as index 
        if current_sum not in prefix_sum:
            prefix_sum[current_sum]=1
        else:
            prefix_sum[current_sum]+=1
    return count

    
    
    
    
    
    
    
    
    
    
#brute force approch    
    # Step 1: Initialize variables
    # starting_index=0
    # running_sum=0
    # count=0
    # for i in range(starting_index,len(numbers)):
    #     for j in range(i,len(numbers)):
    #         running_sum+=numbers[j]
    #         if running_sum==target:
    #             count+=1
    #     # if i ==(len(numbers)-1):
    #     #     starting_index+=1
    #     running_sum=0
    # return count
            




    # Step 2: Process the numbers


    # Step 3: Count subarrays that match the target


    # Step 4: Return the count
    


# Test cases
print(count_subarrays_target_sum([1, 2, 1, 2], 3))   # Expected: 3
print(count_subarrays_target_sum([1, 1, 1], 2))      # Expected: 2
print(count_subarrays_target_sum([1, -1, 1], 1))     # Expected: 3
print(count_subarrays_target_sum([2, 4, 6], 5))      # Expected: 0
print(count_subarrays_target_sum([], 0))             # Expected: 0