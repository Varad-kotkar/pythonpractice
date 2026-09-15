# Return the number with the second-highest frequency. 
# If there is no second frequency, 
# return None
def second_most_frequent(numbers):
    most=None
    sec_most=0
    seen={}
    result=None
    for num in numbers:
        if num not in seen:
            seen[num]=1
        else:
            seen[num]+=1       
        
    for key , value in seen.items():
        if most is None or value>most:
            most=value
    for key , value in seen.items():
        if  value>sec_most and value<most:
            sec_most=value
            result=key
    return result







    # for num in numbers:
    #     if most is None or num>most:
    #         most=num
    # for num in numbers:
    #     if sec_most is None or num>sec_most and num<most:
    #         sec_most=num
    # return sec_most 

print(second_most_frequent([1, 1, 2, 2, 2, 3]))
# expected: 1

print(second_most_frequent([4, 4, 5, 5, 5, 6, 6, 6, 6]))
# expected: 5

print(second_most_frequent([1, 2, 3]))
# expected: 2

print(second_most_frequent([5, 5, 5]))
# expected: None

print(second_most_frequent([]))
# expected: None