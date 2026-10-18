numbers = [2, 4, 6, 8, 10]
window_size = 3

for start in range(len(numbers) - window_size + 1):
    window = numbers[start:start+window_size]
    print(sumwindow)