# Return the maximum sum of a contiguous subarray.
def find_max_subarray_sum(numbers):
    if not numbers:
        return 0
    current_sum =numbers[0]
    highest_sum=numbers[0]
    for num in numbers[1:]:
        # if current_sum is None :
        #     current_sum=num
        if current_sum+num >  num :
            current_sum+=num
        else:
            current_sum=num
        if current_sum>highest_sum:
            highest_sum=current_sum
    return highest_sum
        



print(find_max_subarray_sum([1, 2, 3, 4]))
# expected: 10

print(find_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5]))
# expected: 6

print(find_max_subarray_sum([-5, -2, -8]))
# expected: -2

print(find_max_subarray_sum([5]))
# expected: 5