import numpy as np
import pandas as pd
import os
import re
import sys
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
    with open(name, 'rb') as f:
        return pickle.load(f)


def save_obj(obj, name):
    with open(name, 'wb') as f:
        pickle.dump(obj, f, pickle.
def generate_syllable_freq_dict_from_fHIGHEST_PROTOCOL)


def generate_syllable_freq_dict_from_file():
    syl_count_dict = {}
    regex_pa = r'([^i,y,e,a,o,ó,u,ą,ę]{1,3}[i,y,e,a,o,ó,u,ą,ę]{1})'
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
    if os.path.isfile(dict_pickle_filename):
        return load_obj(dict_pickle_filename)
    else:
        print("Haven't found", dict_pickle_filename, "try to generate it from", dict_filename)
        if os.path.isfile(dict_filename):
            syllable_freq_dict = generate_syllable_freq_dict_from_file()
            save_obj(syllable_freq_dict, dict_pickle_filename)
            return syllable_freq_dict
        else:
            print("Nor", dict_filename, "found. Exiting.")


def create_generator(syllable_freq_dict):
    # to do - try this below
    # stats.rv_discrete(name='custm', values=(syl_count_dict.keys(), list(syl_count_dict.values())/counter))
    pass



if __name__ == "__main__":
    syllable_freq_dict = load_syllable_freq_dict()
    create_generator(syllable_freq_dict)
    print(syllable_freq_dict)