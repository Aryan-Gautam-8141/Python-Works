words = {
    "kya": "what",
    "hai": "is",
    "tum": "you",
}

word = input("Enter a Hindi word: ")

# nice method for searching in dictionary
# print(words[word])    #if word not found, it will raise KeyError and stop the program
print(words.get(word, "Word not found in dictionary."))