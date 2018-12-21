from utils import most_common_words, most_common_nouns, create_bag_of_words, similarity, nearest_coef, nearest_cos, \
    change_to_emb, mean_vectors
from dataset import load_data, load_file_to_string, load_files_to_string, load_vectors, load_paths_from_dir
import os
import pandas as pd

data = 'data/shows'
number_of_words = 100
max_len = 20000

emb_dir = 'embedding/'
emb_file = 'wiki.en'


show_list = ["Taboo", "Game of Thrones"]

names, paths = load_paths_from_dir(data, show_list)
print(names)

movies_common_words = []

print("Most common words.")
for path in paths:
    print(path)
    print(most_common_nouns(load_files_to_string(path, how_many=10), number_of_words))
