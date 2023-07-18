'''
KMP - Knuth-Morris-Pratt Algorithm

A string search algorithm that uses information about the pattern, specifically, the prefixes and suffixes of the pattern, to skip characters in the text where the pattern cannot match. 

Method:
- Compute the prefix function by finding, up to each index, the length of the longest proper suffix that is also a proper prefix in the pattern.
- Use the pre-computed values in the prefix function to perform faster pattern-matching via the Knuth-Morris-Pratt algorithm in the text.

Note a comparison to Robin-Karp (rolling hash can be found at the bottom).
'''


import time
from search_rolling_hash import rabin_karp_algorithm


def prefix_function(pattern):
    pi = [0 for i in range(len(pattern))]
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while (j > 0 and pattern[i] != pattern[j]):
            j = pi[j - 1]
        if (pattern[i] == pattern[j]):
            j += 1
        pi[i] = j
    return pi


def kmp_algorithm(pattern, text):
    m = len(pattern)
    n = len(text)
    pi = prefix_function(pattern)
    j = 0
    count = 0
    for i in range(n):
        while (j > 0 and pattern[j] != text[i]):
            j = pi[j - 1]
        if (pattern[j] == text[i]):
            j += 1
        if (j == m):
            count += 1
            j = pi[j - 1]
    return count


print("\nTEST 1\n")
pattern = ""
for i in range(1000):
    pattern += "A"
text = ""
for i in range(100000):
    text += "A"
start_time = time.time()
print("Matches found: ", rabin_karp_algorithm(pattern, text))
print("Rabin-Karp took %s seconds" % (time.time() - start_time))
start_time = time.time()
print("Matches found: ", kmp_algorithm(pattern, text))
print("KMP took %s seconds" % (time.time() - start_time))

print("\nTEST 2\n")
pattern = "ababbabbabbababbabb"
text = 100000*pattern
start_time = time.time()
print("Matches found: ", rabin_karp_algorithm(pattern, text))
print("Rabin-Karp took %s seconds" % (time.time() - start_time))
start_time = time.time()
print("Matches found: ", kmp_algorithm(pattern, text))
print("KMP took %s seconds" % (time.time() - start_time))
