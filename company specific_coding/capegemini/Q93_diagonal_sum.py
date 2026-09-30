# QUESTION:
# Write a function to find the sum of the main diagonal
# of a square matrix.
#
# Example:
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# → 15
#
# Main diagonal: 1 + 5 + 9


def diagonal_sum(matrix):
    total =0
    # result=[]
    for i in range(len(matrix)):
        total+=matrix[i][i]
    # result.append(total)
    # return result
    return total



# TEST CASES
print(diagonal_sum([[1,2,3],[4,5,6],[7,8,9]]))
# Expected: 15

print(diagonal_sum([[5,1],[2,4]]))
# Expected: 9