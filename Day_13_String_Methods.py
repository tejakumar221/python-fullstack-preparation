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

#print("Method - find()")
"""word = input("Enter the word: ")
character =input("Enter the character: ")
if character in word: 
    character_position = word.find(character)
    print(f"The character '{character}' is found at position {character_position} ")
else:
    print(f"The character {character} is not found")"""

"""sentence = input("Enter a sentence: ")
word = input("Enter the word: ")
if word in sentence:
    word_position = sentence.find(word)
    print(f"The '{word}' is found at index {word_position}")
else:
    print(f"The '{word}' is not found")"""

"""print("String Method - Replace() - needs two parameters, old value, new value")
sentence = input("Enter a sentence: ")
new_sentence = sentence.replace(" ", "-")
print(f"The new sentence is {new_sentence}")

sentence = input("Enter a sentence: ")
existing_word = input("Enter an existing word from the sentence to replace: ")
if existing_word in sentence:   
    new_word = input("Enter the new word to replace the existing word: ")
    new_sentence = sentence.replace(existing_word, new_word)
    print(f"The new sentence is '{new_sentence}'")
else:
    print(f"The word is not present in the sentence")"""

"""print("String Method -- Upper case and lower case conversion")
sentence = input("Enter the sentence: ")
upper_case_sentence = sentence.upper()
print(f"The upper case sentence is '{upper_case_sentence}'")
lower_case_sentence = upper_case_sentence.lower()
print(f"The lower case sentence is '{lower_case_sentence}'")"""

"""print("String Method -- Upper Case and Count of Upper")
sentence = input("Enter the sentence: ")
print(f"The original sentence is '{sentence}'")
upper_case_sentence = sentence.upper()
print(f"The Upper Case sentence is '{upper_case_sentence}'")
upper_case_count = 0
for character in upper_case_sentence:
    if character.isupper():
        upper_case_count += 1
print(f"The Total number of upper case count: {upper_case_count}")"""

"""print("String Method - lower coversion and lower case letters count")
sentence = input("Enter the sentence: ").upper()
print(f"The original sentence is '{sentence}'")
lower_case_sentence = sentence.lower()
print(f"The lower case sentence is '{lower_case_sentence}'")
lower_case_count = 0
for char in lower_case_sentence:
    if char.islower():
        lower_case_count += 1
print(f"The toal number of lower case letters are: {lower_case_count}")"""

"""print("String Method - title()")
sentence = input("Enter a sentence: ")
print(f"The original sentence: '{sentence}'")
title_sentence = sentence.title()
print(f"The titled sentence: {title_sentence}")
words_list = sentence.split()
print(words_list, end = " ")
print()
words_count = len(words_list)
print(f"Words: {words_count}")"""

"""print("String method - capitalize()")
sentence = input("Enter a sentence: ")
print(f"The original sentence is '{sentence}'")
title_sentence = sentence.title()
print(f"The titled sentence is '{title_sentence}'")
capital_sentence = sentence.capitalize()
print(f"The capitalized sentence is '{capital_sentence}'")"""

"""print("String Method - swapcase()")
sentence = input("Enter the sentence: ")
print(f"The original sentence is '{sentence}'")
upper_case_sentence = sentence.upper()
print(f"The upper case sentence is '{upper_case_sentence}'")
lower_case_sentence = upper_case_sentence.lower()
print(f"The lower case sentence is '{lower_case_sentence}'")
title_sentence = sentence.title()
print(f"The title sentence is '{title_sentence}'")
capital_sentence = sentence.capitalize()
print(f"The capitalized sentence is '{capital_sentence}'")
swapcase_sentence = sentence.swapcase()
print(f"The swap cased sentence is '{swapcase_sentence}'")"""

"""print("String methods - isalpha()")
sentence = input("Enter a sentence: ")
if sentence.isalpha():
    print(f"The sentence contains only alphabets")
else:
    print(f"The sentence doesn't contain only alphabets")"""

#print("String method - isdigit()")
"""value = input("Enter a value: ")
if value.isdigit():
    print(f"'{value}' contians only digits")
else:
    print(f"'{value}' does not contain only digits")"""

"""age = input("Enter the age: ")
print(f"The type of age is {type(age)}")
if age.isdigit():
    age = int(age)
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not Eligible to vote")
else:
    print("Please enter digits only")"""

"""print("String Method - isalnum()")
value = input("Enter a word: ")
if value.isalnum():
    print(f"The value '{value}' contains only alphabets and digits")
else:
    print(f"The value '{value}' doesn't contains only alphabets and digits")

username = input("Enter the username: ")
if username.isalnum():
    print("Valid username")
else:
    print("Invalid usernmae")"""

"""print("String method - isupper()")
word = input("Enter a word: ")
if word.isupper():
    print("The word is completely uppercase")
else:
    print("The word is not completely uppercase")

sentence = input("Enter the sentence: ")
print(f"Original sentencee: '{sentence}'")
upper_case_sentence = sentence.upper()
print(f"Upper case sentence: '{upper_case_sentence}'")
print(f"Original sentence already uppercase: {sentence.isupper()}")
print(f"Converted sentence uppercase: {upper_case_sentence.isupper()}")"""

"""print("String Method - islower()")
word = input("Enter a word: ")
if word.islower():
    print("The word is completely lower")
else:
    print("The word is not completely lower")

sentence = input("Enter a sentence: ")
print(f"Original sentence: '{sentence}'")
lower_case_sentence = sentence.lower()
print(f"Lower case sentence: '{lower_case_sentence}'")
print(f"Original sentence already lowercase: {sentence.islower()}")
print(f"Converted sentence lowercase: {lower_case_sentence.islower()}")"""

"""print("String Method - isspace()")
value = input("Enter a value: ")
if value.isspace():
    print("The value contains only spaces")
else:
    print("The value does not contain only spaces")

username = input("Enter a username: ")
if username.isspace():
    print("Invalid user name")
else:
    print("Valid user name")"""

"""print("String Methods - startswith()")
word = input("Enter a word: ")
prefix = input("Enter the starting text: ")
if word.startswith(prefix):
    print(f"The word '{word}' starts with '{prefix}'")
else:
    print(f"The word '{word}' does not start with '{prefix}'")"""

"""sentence = input("Enter a sentence: ")
print(f"The original sentence : {sentence}")
start_word = input("Enter the starting word: ")
print(f"The original sentence starts with '{start_word}': {sentence.startswith(start_word)}")

print("String Method - endswith()")
word = input("Enter a word: ")
suffix = input("Enter the ending text: ")
if word.endswith(suffix):
    print(f"The word '{word}' ends with '{suffix}'")
else:
    print(f"The word '{word}' does not end with '{suffix}'")

print(f"The word '{word}' endswith '{suffix}' : {word.endswith(suffix)}")"""

"""print("--- String Method - strip() ---")
sentence = input("Enter a sentence: ")
print(f"Original sentence: '{sentence}'")
print(f"Length before strip: {len(sentence)}")
clean_sentence = sentence.strip()
print(f"Sentence after strip: '{clean_sentence}'")
print(f"Length after strip: {len(clean_sentence)}")

name = input("Enter your name: ")
clean_name = name.strip()
if clean_name == "":
    print("Invalid name")
else:
    print("Valid name")"""

sentence = input("Enter a sentence: ")

print(f"Original : '{sentence}'")
print(f"lstrip() : '{sentence.lstrip()}'")
print(f"rstrip() : '{sentence.rstrip()}'")
print(f"strip()  : '{sentence.strip()}'")