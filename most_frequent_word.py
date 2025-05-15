# 7. Find the Most Frequent Word
# Problem: Write a function that takes a string and returns the most frequently occurring word.

from collections import Counter

def most_frequent_word(text):
    words = text.split()
    counter = Counter(words)
    print("counter:", counter, "\n")
    print("most common", counter.most_common,"\n", counter.most_common(1))
    return counter.most_common(1)[0][0]

text = "apple banana apple orange apple banana"
print(most_frequent_word(text))


