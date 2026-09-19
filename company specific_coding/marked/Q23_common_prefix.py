# QUESTION:
# Write a function to find the longest common prefix
# among a list of strings.
#
# Example:
# ["flower", "flow", "flight"] → "fl"
#
# If there is no common prefix, return "".


def common_prefix(arr):
    shortest=min(len(s)for s in arr)
    prefix=[]
    for i in range(shortest):
        # for s in arr:
            # if arr[0][i]==s[i]: 
        if all(s[i] == arr[0][i] for s in arr):
            prefix.append(arr[0][i])
        else:
            return ''.join(prefix)
    return ''.join(prefix)



# TEST CASES
print(common_prefix(["flower", "flow", "flight"]))  # Expected: "fl"
print(common_prefix(["dog", "racecar", "car"]))     # Expected: ""
print(common_prefix(["interview", "internet", "internal"]))  # Expected: "inter"
print(common_prefix(["apple", "apple", "apple"]))   # Expected: "apple"