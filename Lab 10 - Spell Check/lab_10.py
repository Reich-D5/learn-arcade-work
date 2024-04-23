import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary_file = open('dictionary.txt', 'r')
dictionary_list = dictionary_file.read().splitlines()
dictionary_file.close()

print("---Linear Search---")

alice_file = open("AliceInWonderLand200.txt", 'r',)

line_number = 0

for line in alice_file:
    line_number += 1
    word_list = split_line(line)

    for word in word_list:
        found = False
        for dictionary_word in dictionary_list:
            if dictionary_word.upper() == word.upper():
                found = True
                break

        if not found:
            print(f"Line {line_number}: {word}")

alice_file.close()

print("---Binary Search---")

alice_file = open('AliceInWonderLand200.txt', 'r')
line_number = 0

for line in alice_file:
    line_number += 1
    word_list = split_line(line)

    for word in word_list:
        low = 0
        high = len(dictionary_list) - 1
        found = False

        while low <= high:
            mid = (low + high) // 2
            if dictionary_list[mid].upper() < word.upper():
                low = mid + 1
            elif dictionary_list[mid].upper() > word.upper():
                high = mid - 1
            else:
                found = True
                break
        if not found:
            print(f"Line {line_number}: {word}")

alice_file.close()
