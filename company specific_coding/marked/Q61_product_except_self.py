# QUESTION:
# Write a function that returns an array where each element
# is the product of all elements except itself.
#
# Do not use division.
#
# Example:
# [1, 2, 3, 4] → [24, 12, 8, 6]


def product_except_self(arr):
  
    # product=1
    result=[]
    for i in range(len(arr)):
        product=1
        for j in range(len(arr)):
            if j!=i:
                product*=arr[j]
            # else:
            #     product=1
        result.append(product)

    return result
                



# TEST CASES
print(product_except_self([1, 2, 3, 4]))  # Expected: [24, 12, 8, 6]
print(product_except_self([2, 3, 4]))     # Expected: [12, 8, 6]
print(product_except_self([1, 2, 3]))     # Expected: [6, 3, 2]