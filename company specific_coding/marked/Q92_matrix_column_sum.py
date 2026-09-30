# QUESTION:
# Write a function to find the sum of each column in a 2D matrix.
#
# Example:
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# → [12,15,18]


def column_sums(matrix):
    # col=0
    result=[]
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[i])):
    #         col+=matrix[j][i]
    #     result.append(col)
    #     col=0
    # return result
    for j in range(len(matrix[0])):      # columns
        col = 0
        for i in range(len(matrix)):     # rows
            col += matrix[i][j]
        result.append(col)
    return result

# TEST CASES
print(column_sums([[1,2,3],[4,5,6],[7,8,9]]))
# Expected: [12,15,18]

print(column_sums([[1,2],[3,4]]))
# Expected: [4,6]