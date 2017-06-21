my_sentence = "This is a pen"
print my_sentence

words = my_sentence.split(" ")
for word in words:
    print(word)

print("|".join(words))
