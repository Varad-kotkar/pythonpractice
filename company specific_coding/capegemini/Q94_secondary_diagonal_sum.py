# QUESTION:
# Write a function to find the sum of the secondary diagonal
# of a square matrix.
#
# Example:
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# → 15
#
# Secondary diagonal: 3 + 5 + 7


def secondary_diagonal_sum(matrix):
    # total=0
    # j=len(matrix[0])
    # for i in range(len(matrix),0):
        # for j in range(len(matrix[0])):            
        # total+= matrix[i][i]
    total=0
    i=0
    j=len(matrix[0])-1
    while i<len(matrix) and j >= 0:
        total+= matrix[i][j]
        i+=1
        j-=1
    return total

# TEST CASES
print(secondary_diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
# Expected: 15

print(secondary_diagonal_sum([[1,2],[3,4]]))
# Expected: 5