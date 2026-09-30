# QUESTION:
# Write a function to find the transpose of a matrix.
#
# The transpose converts rows into columns.
#
# Example:
# [[1,2,3],
#  [4,5,6]]
#
# →
# [[1,4],
#  [2,5],
#  [3,6]]


def transpose(matrix):
    # matric=[]
    # i=0
    # j=0
    # while i <len(matrix) and j <len(matrix[0]):
    #    while i <len(matrix):
    #     matric.append(matrix[i][j])
    #     i+=1

    #    j+=1
    #    i=0
    # return matric
    result = []

    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)

    return result
# TEST CASES
print(transpose([[1,2,3],[4,5,6]]))
# Expected: [[1,4],[2,5],[3,6]]

print(transpose([[1,2],[3,4]]))
# Expected: [[1,3],[2,4]]