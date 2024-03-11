def get_words(length):
    dictionary = open('twl98.txt')
    words = dictionary.readlines()
    dictionary.close()
    output = []
    for word in words:
        word = word.strip()
        if len(word) == length:
            output.append(word)
    return output