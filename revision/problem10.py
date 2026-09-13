def second_largest(numbers):
    try :
        largest=numbers[0]
        second_largest_num=None
        for num in numbers:
            if num>largest:
                second_largest_num=largest
                largest=num
            
            elif num<largest and ( second_largest_num is None or num > second_largest_num) :
                second_largest_num=num
        return second_largest_num
    except IndexError:
        return None
        
    

    

print(second_largest([-1]))
print(second_largest([]))
print(second_largest([4, 4, 2, 1]))