'''
Naive pattern search:

Iterates through text. for each character, iterates through the pattern you are looking for. if the first character of the pattern matches, it checks the second of the pattern against text[index+1]. 

if there is any failure, it breaks the loop and moves onto the next character in the text.

if it successfully reaches the end of the pattern without
'''


def pattern_search(text, pattern):

    for index in range(len(text)):

        match_count = 0

        for char in range(len(pattern)):

            if text[index + char] == pattern[char]:
                match_count += 1

            else:
                break

        if match_count == len(pattern):
            print(pattern, "found at index", index)


text = "------NEEDLE-------NEEDLE---------NEEDLE"
pattern = "NEEDLE"
pattern_search(text, pattern)
