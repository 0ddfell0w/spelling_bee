import json
import requests as r
import sys
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python solve_spelling_bee.py <letters_with_center_letter_first>")
    else:
        problem = sys.argv[1]
        words = r.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json').json().keys()
        letters = {c for c in problem}
        required = problem[0]
        answers = {word for word in words if required in word and len(word) > 3 and all(l in letters for l in word)}
        for answer in sorted(answers, key=len, reverse=True):
            print(answer)
