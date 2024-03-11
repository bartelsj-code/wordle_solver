def get_words2(length):
    dictionary = open('words.txt')
    lines = dictionary.readlines()
    line = lines[0]
    words = line.split(', ')
    dictionary.close()
    output = []
    for word in words:
        word = word.strip().upper()
        if len(word) == length:
            output.append(word)
    return output