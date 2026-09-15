'''Return the number of words that start with a vowel.

Examples:

"apple banana orange" → 2
"hello world" → 0
"apple elephant ice" → 3
"" → 0

Treat these as vowels:

a e i o u

Both uppercase and lowercase should work:

"Apple dog Orange" → 2
🧠 Think first

You need to combine things you already know:

string
  ↓
split into words
  ↓
loop through words
  ↓
check first character
  ↓
count matches

For:

"apple banana orange"

think:

apple  → a → vowel ✅
banana → b → ❌
orange → o → vowel ✅'''
def count_words_starting_with_vowel(text):
    text= text.split()
    vowels=["a","e",'i','o','u']
    count=0
    for i in text:
        i=i.lower()
        if i[0] in vowels:
            count+=1 
    return count

print(count_words_starting_with_vowel("apple banana orange"))
        