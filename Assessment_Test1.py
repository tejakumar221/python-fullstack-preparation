"""print("Q.No. 1 Program to count total vowels and consonants in a word")
word = input("Enter a word: ")
count_vowels = 0
count_consonants = 0
for char in word:
    if char.isalpha():
        if char in "aeiouAEIOU":
            count_vowels += 1
        else:
            count_consonants += 1
print(f"Total vowels: {count_vowels}")
print(f"Total consonants: {count_consonants}")

print("Q.No.2 Find total Alphabets, digits, spaces and special character:")
sentence = input("Enter a sentence: ")
count_alphabets = 0
count_digits = 0
count_space = 0
count_special_characters = 0
for char in sentence:
    if char.isalpha():
        count_alphabets += 1
    elif char.isdigit():
        count_digits += 1
    elif char.isspace():
        count_space += 1
    else:
        count_special_characters += 1
print(f"Total Alphabets: {count_alphabets}")
print(f"Total Digits: {count_digits}")
print(f"Total spaces: {count_space}")
print(f"Total Special Character: {count_special_characters}")"""

print("Q.No.3 Find Total words, longest word, shorted word, average length of word")
sentence = input("Enter a sentence: ")
print(f"Original sentence: {sentence}")
words_sentence = sentence.split()
print(f"Words in sentence: {words_sentence}")
total_words_sentence = len(words_sentence)
print(f"Total number of words in the sentence: {total_words_sentence}")
char_count = 0
longest_word = words_sentence[0]
shortest_word = words_sentence[0]
for word in words_sentence:
    if len(word) > len(longest_word):
        longest_word = word
    elif len(word) < len(shortest_word):
        shortest_word = word
    for char in word:
        char_count += 1

print(f"The total characters: {char_count}")
print(f"The longest word: {longest_word}")
print(f"The shortest word: {shortest_word}")
print(f"Average length of words: {char_count / total_words_sentence}")


