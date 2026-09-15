# Return two lists: even numbers first, odd numbers second.
def separate_even_odd(numbers):
    even=[]
    odd=[]
    result=[]
    for num in numbers:
        if num %2==0:
            even.append(num)
        else:
            odd.append(num)
    result.append(even)
    result.append(odd)
    return result

print(separate_even_odd([1, 2, 3, 4, 5, 6]))
# expected: [[2, 4, 6], [1, 3, 5]]

print(separate_even_odd([2, 4, 6]))
# expected: [[2, 4, 6], []]

print(separate_even_odd([1, 3, 5]))
# expected: [[], [1, 3, 5]]

print(separate_even_odd([]))
# expected: [[], []]