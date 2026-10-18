# QUESTION:
# Given an array and a window size k, find the sum of every
# group of k consecutive elements using the sliding window pattern.

def sliding_window_sums(nums, k):
    result=[]
    # Window=0
    Window=sum(nums[0:0+k])
    result.append(Window)
    for start in range(k,len(nums)):
        # Window=nums[start:start+k]
        # # Window=Window+nums[start]-nums[start-k]
        # result.append(sum(Window))
        Window=Window+nums[start]-nums[start-k]
        result.append(Window)

        # for j in range (k):
        #     total=total+nums[i]
        # while k>k:
        #     new_total=total+nums[k+1]-nums[0]
        # result.append(new_total)
    return result


# IMPORTANT TEST CASES

print(sliding_window_sums([2, 4, 6, 8], 3))
# Expected: [12, 18]

print(sliding_window_sums([1, 2, 3, 4, 5], 2))
# Expected: [3, 5, 7, 9]

print(sliding_window_sums([5, 5, 5, 5], 2))
# Expected: [10, 10, 10]

# print(sliding_window_sums([7], 1))
# # Expected: [7]

# print(sliding_window_sums([1, 2], 3))
# # Expected: []

# print(sliding_window_sums([], 2))
# # Expected: []