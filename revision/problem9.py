def count_above_average(numbers):
    total=0
    num_count=len(numbers)
    above_avg=0

    for num in numbers:
        total+= num
        # num_count=len(numbers)
    if num_count!=0:
        avg=total/num_count
    for num in numbers:
        if num >avg:
            above_avg+=1
    return above_avg
print(count_above_average([10, 20, 30]))
print(count_above_average([1, 2, 3, 4]))
print(count_above_average([5, 5, 5]))
print(count_above_average([]))