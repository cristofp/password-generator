import numpy as np
import pandas as pd
import os
import pkg_resources
import re
import sys
from random import randint
from scipy import stats
import pickle

# constants
dict_filename = "slowa.txt"
dict_pickle_filename = "dict_pickle.pkl"


# Get password length from cmd
# read polish dictionary
# go through all df creating dictionary of all
# transform dict to df
# sort df according to values
# save it as csv



# syl_count_df = pd.DataFrame(syl_count_dict, index=['syllable', 'amount'])
# syl_count_df.sort_values(['syllable'])



def load_obj(name):
    return pickle.load(name)

def save_obj(obj, name):
    with open(name, 'wb') as f:
        pickle.dump(obj, f)


def generate_syllable_freq_dict_from_file(count):
    syl_count_dict = {}
    regex_pa = r'([^i,y,e,a,o,ó,u,ą,ę]{%d}[i,y,e,a,o,ó,u,ą,ę]{1})' % count
    print(regex_pa)
    counter = 0
    with open(dict_filename, 'rb') as polish_words_file:
        for word in polish_words_file.readlines():
            for result in re.finditer(regex_pa, word.strip().decode('utf-8')):
                letter_group = result.group(1)
                letter_group_count = syl_count_dict.get(letter_group, 0)
                letter_group_count += 1
                syl_count_dict[letter_group] = letter_group_count
                counter += 1
    syl_count_dict.update((word, quantity / counter) for word, quantity in syl_count_dict.items())
    return syl_count_dict


def load_syllable_freq_dict():
    return (load_obj(pkg_resources.resource_stream(__name__, 'dict_pickle.pkl')))

def get_syl_with_chars_count(syllable_freq_dict, count):
    return dict((key, value) for key, value in syllable_freq_dict.items() if len(key) == count)


def createRVSReadyDict(syllable_freq_dict):
    dict = {}
    item = 0
    for (key, value) in syllable_freq_dict.items():
        dict[item] = (key, value)
        item += 1
    return dict


def create_generator(syl_count_dict):
    probabilities = []

    for (_, probability) in syl_count_dict.values():
        probabilities.append(probability)

    return stats.rv_discrete(name='custm', values=(list(syl_count_dict.keys()), probabilities))


def generatePasswordPart(length, rvsDict, generators):
    return rvsDict[length][generators[length].rvs(size=1)[0]][0]


def getPartsLengthArrayForLength(length):
    parts = []
    while length > 0:
        if length <= 4:
            to_push = length
        else:
            to_push = randint(2, 4)
        parts.append(to_push)
        length -= to_push
    return parts


if __name__ == "__main__":
    try:
        passwordLength = int(sys.argv[1])
    except Exception:
        print("Length not specified using 10")
        passwordLength = 10

    tuples = load_syllable_freq_dict()

    rvsReadyDict = {2: createRVSReadyDict(tuples[0]),
                    3: createRVSReadyDict(tuples[1]),
                    4: createRVSReadyDict(tuples[2])}

    charsToRv = {2: create_generator(rvsReadyDict[2]),
                 3: create_generator(rvsReadyDict[3]),
                 4: create_generator(rvsReadyDict[4])}

    passwordParts = getPartsLengthArrayForLength(passwordLength)

    password = ""

    for partLength in passwordParts:
        password += generatePasswordPart(partLength, rvsReadyDict, charsToRv)

    print(password)
