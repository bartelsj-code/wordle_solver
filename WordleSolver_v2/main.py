import string
import csv
import math
from time import perf_counter
import os

class Solver:
    def __init__(self):
        self.words = []
        self.get_allowed_words()
        self.guess_dict = {}
        self.evaluated = {}

    def set_start(self, sw):
        self.start_word = sw
        self.mem_file = f"{self.start_word}.csv"
        

    def stringify(self, guess, result):
        out = ""
        for i in range(5):
            out += str(result[i])
        output = guess+out
        return output
    
    def populate_dict(self):
        try:
            f = open(self.mem_file, "r")
        except:
            f = open(self.mem_file, "w")
            writer = csv.writer(f, lineterminator="\n")
            writer.writerow(["",self.start_word])
            f.close()
            f = open(self.mem_file, "r")

        csv_reader = csv.reader(f)
        for line in csv_reader:
            self.guess_dict[line[0]] = line[1]
        f.close()

    def store_dict(self):
        f = open(self.mem_file, "w")
        writer = csv.writer(f, lineterminator="\n")
        for guess in self.guess_dict:
            writer.writerow([guess, self.guess_dict[guess]])
        f.close()

    def play(self):
        self.populate_dict()
        str_rep = ""
        self.remaining_words = self.words[:]
        for i in range(10):
            if str_rep in self.guess_dict:
                guess = self.guess_dict[str_rep]
            else:
                guess = self.get_next_guess()
                self.guess_dict[str_rep] = guess
                self.store_dict()
            if len(self.remaining_words) < 10: 
                print(self.remaining_words)
            print("play \'{}\'".format(guess))
            real_result = self.get_result()
            str_rep += self.stringify(guess,real_result)
            self.elimintate_words(guess, real_result)
            if str_rep in self.guess_dict:
                guess = self.guess_dict[str_rep]
            else:
                guess = self.get_next_guess()
                self.guess_dict[str_rep] = guess
                self.store_dict()
            

    def matches_clue(self, guess_word, possible_word, clue):
        result = self.get_clue(guess_word, possible_word)
        if result == clue:
            return True
        return False


    def elimintate_words(self, guess, result):
        not_eliminated = []
        for word in self.remaining_words:
            if self.matches_clue(guess, word, result):
                not_eliminated.append(word)
        self.remaining_words = not_eliminated

    def get_result(self):
        str = input("guess result: ")
        lst = str.split(',')
        lst2 = []
        for chr in lst:
            lst2.append( int(chr))
        return lst2

    def stringer(self, clue):
        return self.stringify('',clue)
        
    def get_next_guess(self):
        
        allowed_guesses = self.all_words
        # allowed_guesses = self.remaining_words
        start = perf_counter()
        i = 1

        upper_bound = len(allowed_guesses)

        best_word = self.remaining_words[0]
        remaining_length = len(self.remaining_words)
        most_elminations = 0
        old_completion = -1

        
        for potential_guess in allowed_guesses:
            self.evaluated = {}
            
            completion = math.floor(1000*i/upper_bound)
            if completion != old_completion:
                current_time = perf_counter() - start
                total_time = current_time*upper_bound/i
                remaining_time = math.floor(total_time - current_time)
                hours, minutes, seconds = remaining_time//3600, (remaining_time%3600)//60, remaining_time%60
                print("{}% done.   Current best:{}   Time Remaining: {}h{}m{}s              ".format(completion/10, best_word, hours, minutes, seconds), end = "\r")
            old_completion = completion
            i+=1
            eliminated = 0
            for possible_solution in self.remaining_words:
                clue = self.get_clue(potential_guess, possible_solution)
                clue_string = self.stringer(clue)
                if clue_string in self.evaluated:
                    pass
                else:
                    count = 0
                    for tres in self.remaining_words:
                        if self.matches_clue(potential_guess, tres, clue):
                            pass
                        else:
                            count += 1
                    self.evaluated[clue_string] = count
                eliminated += self.evaluated[clue_string]
            if eliminated > most_elminations:
                best_word = potential_guess
                most_elminations = eliminated
            if eliminated == most_elminations:
                if best_word in self.remaining_words:
                    pass
                else:
                    best_word = potential_guess
        print()
        return best_word


    def get_allowed_words(self):
        file = open("twl98.txt", "r")
        words = file.readlines()
        file.close()
        output = []
        for word in words:
            word = word.strip().lower()
            if len(word) == 5:
                output.append(word)
        self.all_words = output

    def get_five_letter_words(self):
        file = open("words.txt")
        line = file.readline()
        words = line.split(",")
        output = []
        for word in words:
            word = word.strip()
            output.append(word)
        # file = open("twl98.txt", "r")
        # words = file.readlines()
        # file.close()
        # output = []
        # for word in words:
        #     word = word.strip()
        #     if len(word) == 5:
        #         output.append(word)
        self.words = output

    def get_clue(self, guess, solution):
        clue = [0,0,0,0,0]
        solution_marked = [False, False, False, False, False]
        for i in range(5):
            if guess[i] == solution[i]:
                clue[i] = 2
                solution_marked[i] = True
        for i in range(5):
            if clue[i] != 2:
                for b in range(5):
                    if not solution_marked[b] and guess[i] == solution[b]:
                        clue[i] = 1
                        solution_marked[b] = True
        return clue

def main():

    solver = Solver()
    solver.get_five_letter_words()
    start_word = ''
    while True:
        start_word = str(input("First guess (\"raise\" suggested):  ")).lower()
        if start_word.isalpha() and len(start_word) == 5 and start_word in solver.all_words:
            os.system("cls")
            break
        else:
            os.system("cls")
            print(f"{start_word} is not a possible starting word, try again")
            
    solver.set_start(start_word)
    solver.play()
    

    # print(words)



main()