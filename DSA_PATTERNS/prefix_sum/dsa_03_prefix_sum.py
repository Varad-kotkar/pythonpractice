"""
DSA Pattern: Prefix Sum
Problem 3: Daily Sales Queries

Build a prefix sum array and answer multiple range-sum queries.

Requirements:
- Build the prefix sum array only once.
- Use the same prefix sum array for every query.
- Do not modify the original sales list.
- Do not use sum() or max().
- Return a list containing the answer to each query.
- If sales is empty, return an empty list.

Expected examples:
[10, 20, 30, 40, 50], [(0, 2), (1, 3), (2, 4)]
    -> [60, 90, 120]

[5, 15, 10], [(0, 0), (0, 2), (1, 2)]
    -> [5, 30, 25]

[], [(0, 0)]
    -> []
"""


def build_prefix_sum(sales):
    running_sum=0
    prefix=[]
    for sale in sales:
        running_sum+= sale
        prefix.append(running_sum)
    return prefix


def answer_queries(sales, queries):
    if sales== []:
        return []
    sales=build_prefix_sum(sales)
    result=[]
    # if sales== 0:
    #     return [(0, 0)]
    for  query in queries:
        if query[0]==0:
            result.append(sales[query[1]])
        else:
            result.append(sales[query[1]]-sales[query[0]-1])
    return result


# TEST CASES

print(answer_queries(
    [10, 20, 30, 40, 50],
    [(0, 2), (1, 3), (2, 4)]
))  # Expected: [60, 90, 120]

print(answer_queries(
    [5, 15, 10],
    [(0, 0), (0, 2), (1, 2)]
))  # Expected: [5, 30, 25]

print(answer_queries(
    [],
    [(0, 0)]
))  # Expected: []

print(answer_queries(
    [7],
    [(0, 0), (0, 0)]
))  # Expected: [7, 7]