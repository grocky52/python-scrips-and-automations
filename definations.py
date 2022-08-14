#!/usr/bin/python3
from PyDictionary import PyDictionary

def find_meaning():
    word = input('enter word:    ')
    dict_obj = PyDictionary()
    word_meaning = dict_obj.meaning(word)
    meaning_details = ''
    if 'Noun' in word_meaning:
        meaning_details += "Noun:\n-" + '\n-'.join(word_meaning['Noun'])
        print(meaning_details)
    if 'verb' in word_meaning:
        meaning_details += 'Verb:\n-' + '\n-'.join(word_meaning['Verb'])
        print(meaning_details)
find_meaning()
