def row_sums(matrix):
    result=[]
    total=0
    for i in matrix:
        for  j in i:
            total+=j
        
        result.append(total)
        total=0
    return result
        


print(row_sums([[1,2,3], [4,5,6], [7,8,9]]))
# [6, 15, 24]