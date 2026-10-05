# Let L be a list of words. You are expected to create different kinds of dictionaries. In each case, think about the right choice of keys and their corresponding values.

#     Create a dictionary that has information on the collection of words that have a specific letter count.
#     Create a dictionary that has information the frequency of occurrence of words in the list L.
#     Create a dictionary that contains information about the list of words that begin with a specific letter. Try to mimic the "English language dictionary" by sorting every list of words that begins with a given letter.

# list of words
L = ["apple","bat","ball","cat","dog","door","ant"]

# 1. dictionary for letter count
D1 = {}
for word in L:
    n = len(word)
    if n not in D1:
        D1[n] = []
    D1[n].append(word)

print("Letter count dictionary:", D1)


# 2. dictionary for word frequency
D2 = {}
for word in L:
    if word not in D2:
        D2[word] = 1
    else:
        D2[word] += 1

print("Word frequency dictionary:", D2)


# 3. dictionary for words starting with same letter
D3 = {}
for word in L:
    first = word[0]
    if first not in D3:
        D3[first] = []
    D3[first].append(word)

for k in D3:
    D3[k].sort()

print("Words by first letter:", D3)