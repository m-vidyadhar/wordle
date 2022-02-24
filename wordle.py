import sys
sys.path.insert(0, "/Users/chintu/Documents/repos/wordle/")

import numpy as np
import pandas as pd
from utility import *


DIR = "/Users/chintu/Documents/repos/wordle/data/"
JSFILE = "main.js"
SOLUTIONS_FILE = "solutions.txt"
DICTIONARY_FILE = "dictionary.txt"


# load_words(DIR+JSFILE, DIR+SOLUTIONS_FILE, DIR+DICTIONARY_FILE)

class Wordle():
    def __init__(self) -> None:
        self.solutions = pd.read_csv(DIR+SOLUTIONS_FILE).words.to_list()
        self.dictionary = pd.read_csv(DIR+DICTIONARY_FILE).words.to_list()
        pass

    def check_match(self, guess, answer):
        if (guess == answer):
            return (True, f"{fprints.OKGREEN}{guess}{fprints.ENDC}")
        
        fchars = ""
        for (g, a) in zip(guess, answer):
            if (g == a):
                fchars += f"{fprints.OKGREEN}{g.upper()}{fprints.ENDC}"
            elif g in answer:
                fchars += f"{fprints.WARNING}{g.upper()}{fprints.ENDC}"
            else:
                fchars += f"{fprints.FAIL}{g.upper()}{fprints.ENDC}"
        return (False, fchars)

    def play(self, sol_idx=None, random=True, n_turns=6):
        if (sol_idx is None) and not random:
            print("Either solution index should not \
                NULL or random should be TRUE!")
            return
        if random:
            sol_idx = np.random.randint(0, len(self.solutions), 1)[0]
        answer = self.solutions[sol_idx]

        turn = 1
        while (turn <= n_turns):
            pretext = "Turn %d: " % turn
            guess = input(pretext).lower()

            if (len(guess) != 5):
                print("Word not in dictionary!\r")
                continue

            if guess in self.dictionary:
                match, fchars = self.check_match(guess, answer)
                print(f"{fprints.PREV_LINE}{pretext}{fchars}")

                if match:
                    print("Completed in %d chances!" % turn)
                    break
                turn += 1

            else:
                print("Word not in dictionary!\r")
        if not match:
            print("Failed!! Answer: %s" % answer)
        pass



if (__name__ == "__main__"):
    api = Wordle()
    api.play()
