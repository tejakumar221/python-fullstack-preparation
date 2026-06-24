print("Q. No. 1")
sentence = input("Enter a sentence: ")
print(f"The original sentence: {sentence}")
words_sentence = sentence.split()
upper_case = sentence.upper()
print(f"The upper case sentence: {upper_case}")
lower_case = sentence.lower()
print(f"The lower case sentence: {lower_case}")
word_count = 0
for word in words_sentence:
    word_count += 1
print(f"The total number of words in '{sentence}': {word_count}")

print("Q. No. 2")
sentence = input("Enter the sentence: ")
print(f"Starts with Python: {sentence.startswith("Python")}")
print(f"Ends with Developer: {sentence.endswith("developer")} ")

print("Q.No.3")
sentence = input("Enter a sentence: ")
print(f"Original Sentence: {sentence}")
existing_word = input("Enter the existing word: ")
new_word = input("Enter the word to be replaced: ")
modified_sentence = sentence.replace(existing_word, new_word)
print(f"Modified Sentence: {modified_sentence}")

print("Q.No.4")
username = input("Enter the username: ")
print(f"Original username: {username}")
modified_username = username.strip()
print(f"Modified username: {modified_username}")
if username != "" and username.isalnum():
    print("Valid Username")
else:
    print("Invalid Username")

print("Q.No.5")
sentence = input("Enter the sentence: ")
length_sentence = len(sentence)
print(f"Lenght: {length_sentence}")
print(f"First character: {sentence[0]}")
print(f"Last character: {sentence[length_sentence - 1]}")
reversed_sentence = " "
for char in sentence:
    reversed_sentence = char + reversed_sentence
print(f"Reversed Sentence: {reversed_sentence}")

print("Q.No.6")
word = input("Enter the word: ")
print(f"Contains only aplhabets: {word.isalpha()}")
print(f"Conttains only digits: {word.isdigit()}")
print(f"Contains both alphabets and digits: {word.isalnum()}")