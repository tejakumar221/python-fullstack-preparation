"""text = input("Enter a word: ")
for character in text:
    print(character, end= " ")
print()
print(text[:len(text)])
print(text[::-1])"""

"""sentence = input("Enter a sentence: ")
words_sentence = sentence.split()
print(f"Split words: {words_sentence}")
print(f"Reversed sentence: {sentence[::-1]}")
print(f"Word Order change: {' '.join(words_sentence[::-1])}")
for word in words_sentence:
    print(word[::-1], end = " ")"""

sentence = input("Enter a word or sentence: ")
original_sentence = sentence
print(f"Original Sentence: {original_sentence}")
reversed_sentence = " "
for character in sentence:
    reversed_sentence = character + reversed_sentence
print(f"Reversed Sentence: {reversed_sentence}")
if original_sentence.lower() == reversed_sentence.lower():
    print("It's a Palindrome")
else:
    print("It's not a Palindrome")

