__author__ = 'Joshua Zosky'
# Random no replacement

import random

def random_no_replacement(item_list):
    new_list = list(item_list)
    random.shuffle(new_list)
    return new_list