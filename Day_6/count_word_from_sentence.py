# Create a program that takes a sentence as input and counts the number of words in it

# sentence = input ("Enter a sentence : ")
# word = sentence.split()
# result = len(word)
# print(result)

# Using function
def count_word(sentence):
    word =sentence.split()
    result = len(word)
    return result
sentence = input ("Enter a sentence : ")
word = count_word(sentence)
print(word)

# Implement a program that swaps the values of two variables