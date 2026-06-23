"""print("--- String Methods- Count() ---")
word = input("Enter a word: ")
sentence = input("Enter a sentence: ")
character_occurance = input("Enter the character: ")
word_occurance = input("Enter the word: ")
print(word.count(character_occurance))
print(sentence.count(word_occurance))

print("2. Count Vowles")
word = input("Enter a word: ")
count_vowels = 0
for character in word:
    if character in "aeiouAEIOU":
        count_vowels += 1
        print(f"{character} : {word.count(character)}")
print(f"The Total Vowels in {word}: {count_vowels}")
print()

print("3. Count Spaces")
sentence = input("Enter a sentence: ")
print(f"Total Spaces: {sentence.count(' ')}")"""

"""print("4. Count Uppercase and Lowercase")
word = input("Enter a word: ")
count_upper = 0
count_lower = 0
for char in word:
    if char.isupper():
        count_upper += 1
        
    elif char.islower():
        count_lower += 1
        
print(f"Upper Case Letters: {count_upper}")
print(f"Lower Case Letters: {count_lower}")"""

"""print("5. Word Occurance")
sentence = input("Enter a sentence: ")
word_sentence = input("Enter the word to be counted: ")
print(f"The word '{word_sentence}' appears {sentence.count(word_sentence)} times.")"""

print("Method - find()")
"""word = input("Enter the word: ")
character =input("Enter the character: ")
if character in word: 
    character_position = word.find(character)
    print(f"The character '{character}' is found at position {character_position} ")
else:
    print(f"The character {character} is not found")"""

sentence = input("Enter a sentence: ")
word = input("Enter the word: ")
if word in sentence:
    word_position = sentence.find(word)
    print(f"The '{word}' is found at index {word_position}")
else:
    print(f"The '{word}' is not found")