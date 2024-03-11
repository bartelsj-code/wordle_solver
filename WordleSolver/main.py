from sorter import *
from sorter2 import *
import random

all_words = get_words2(5)
random.shuffle(all_words)

def suggest_word():
    return all_words[0]
    # possible_words = all_words
    # for word in possible_words:
    #     alt_words = possible_words.copy()
    #     alt_words.remove(word)
    #     for word2 in alt_words:
    #         key = get_key("train", "tiles")


    #         print(key)
    # return all_words[0]

def string_list(word):
    lst = []
    for chr in word:
        lst.append(chr)
    return lst


# def get_key(guess, answer):
#     guess = string_list(guess)
#     key = [None, None, None, None, None]
#     for i in range(len(guess)):
#         if guess[i] == answer[i]:
#             key[i] = "2"
#     for i in range(len(guess)):
#         if answer
#     return key
    


def get_result():
    result = str(input("result here: "))
    result = result.split(",")
    print(result)
    return result

def incorrect(word6, incorrect_letters):
    i = 0
    for character in word6:
        if character in incorrect_letters[i]:
            return True
        i+= 1
    return False


def adjust_list(word, result, incorrect_letters, correct_letters):
    to_be_popped = [word]
    for i in range(len(result)): #maybe -1
        for j in range(len(all_words)):
            word2 = all_words[j]
            if result[i] == "2":
                if word[i] != word2[i]:
    
                    if all_words[j] not in to_be_popped:
                        to_be_popped.append(all_words[ j])
                else:
                    if word[i] not in correct_letters:
                        correct_letters.append(word[i])

            if result[i] == "1":
                if word[i] not in word2 or word[i] == word2[i]:
                    if all_words[j] not in to_be_popped:
                        to_be_popped.append(all_words[ j])

                else:
                    correct_letters.append(word[i])

            if result[i] == "0":
                incorrect_letters[i].append(word[i])
                if word[i] in word2:
                    if word[i] not in correct_letters:
                        if all_words[j] not in to_be_popped:
                            to_be_popped.append(all_words[ j])

    for word6 in all_words:
        if incorrect(word6, incorrect_letters):
            if word6 not in to_be_popped:   
                to_be_popped.append(word6)             

    for word3 in to_be_popped:
        all_words.remove(word3)

    

    return incorrect_letters, correct_letters
    


        
def main():
    word_not_found = True
    correct_letters = []
    incorrect_letters = {0:[],1:[],2:[],3:[],4:[]}
    while word_not_found:
        word = suggest_word()
        print("suggested word: {}".format(word))
        # word = str(input("used word:")).upper()
        result = get_result()
        
        incorrect_letters, correct_letters = adjust_list(word, result, incorrect_letters, correct_letters)
        print("remaining possibilities: {}".format(len(all_words)))
        

main()