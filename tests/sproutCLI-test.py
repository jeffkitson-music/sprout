# from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
from wordlist import bip39 as bip39
import sprout

art = """
                                 _     ____  _      ___ 
 ___  _ __   _ __   ___   _   _ | |_  / ___|| |    |_ _|
/ __|| '_ \ | '__| / _ \ | | | || __|| |    | |     | | 
\__ \| |_) || |   | (_) || |_| || |_ | |___ | |___  | | 
|___/| .__/ |_|    \___/  \__,_| \__| \____||_____||___|
     |_|                                                

"""


questions = [
    {
        'type': 'input',
        'name': 'first_name',
        'message': 'What\'s your first name',
    },
    {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': ['Recover', 'Split'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'list',
        'name': 'keys',
        'message': 'What keys do you have?',
        'choices': ['1 & 2', '1 & 3', "2 & 3"],
        'filter': lambda val: val.lower()
    },
]


def word_input(key):
    i = 1
    words = []
    while i < 25:
        w = input("{}, Word {}: ".format(key, i))
        # try word lookup, also make sure to lower?
        if w.lower() in bip39:
            words.append(w.lower())
        else:
            print()
            print("Invalid or misspelled word! Try again...")
            print()
            i -= 1
        i += 1
    print(words)
    return words


def join_keys():
    key_answer = prompt(questions[2])
    # print(key_answer)
    key_choices = [key_answer["keys"][0], key_answer["keys"][-1]]
    keys = [key_answer["keys"]]
    for choice in key_choices:
        print("=== Key {} ===".format(choice))
        key = word_input("Key {}".format(choice))
        keys.append(key)
    # print(keys)
    return keys


def show_seed(phrase, title):
    print()
    print("=== {} ===".format(title))
    i = 1
    complete_phrase = ""
    for word in phrase:
        print("Word {}: {}".format(i, word))
        complete_phrase = complete_phrase + " " + word
        i += 1
    complete_phrase = complete_phrase.strip()
    print("Complete Phrase: {}".format(complete_phrase))
    print()


def main():
    print(art)
    answers = prompt(questions[1])
    # print_json(answers)  # use the answers as input for your app
    # print(answers)

    if answers["action"] == "recover":
        keys = join_keys()
        seed_phrase = sprout_public.recover_seed(keys[1], keys[2], keys[0])
        # print(seed_phrase)
        show_seed(seed_phrase,title="Original Seed Phrase")
    elif answers["action"] == "split":
        seed_phrase = word_input("Original Seed")
        split_seed = sprout_public.split_seed(seed_phrase)
        i = 1
        for key in split_seed:
            show_seed(key, title="Key {}".format(i))
            i+=1


# Here we go!
main()
