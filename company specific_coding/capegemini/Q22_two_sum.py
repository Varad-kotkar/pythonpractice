# QUESTION:
# Write a function to find two numbers in an array
# whose sum is equal to the target.
#
# Return their indices.
#
# Example:
# [2, 7, 11, 15], target = 9 → [0, 1]


# def two_sum(arr, target):
#     for i in range(len(arr)):
#         for j in range(i + 1,len(arr)):
#             if arr[j]+arr[i]==target:
#                 return i,j

# def two_sum(arr, target):
#     # result=[]
#     for i in range(len(arr)-1):
#         if arr[i]+arr[i+1]==target:
#             # result.append((i,i+1))
#             return i,i+1
def two_sum(arr, target):  
    seen={} 
    for i in range(len(arr)):
        needed = target - arr[i]
        if needed in seen:
            return [seen[needed], i]
        if arr[i] not in seen:
            seen[arr[i]] = i
    


# TEST CASES
print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
print(two_sum([3, 2, 4], 6))       # Expected: [1, 2]
print(two_sum([3, 3], 6))          # Expected: [0, 1]
