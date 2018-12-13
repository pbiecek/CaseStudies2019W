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

df = pd.read_csv('similarities.csv')
df = df.drop('Unnamed: 2', 1)
df = df.dropna(axis='rows')

df_top = df.iloc[0:30, :]
print(df_top)

list_similiar = []
show_list = []

for index, row in df_top.iterrows():
    list_similiar.append(row['similatities'].split(','))
    show_list += row['similatities'].split(',')

show_list += list(df_top['show'])

df_top['sim_list'] = list_similiar

show_list = list(set(show_list))

names, paths = load_paths_from_dir(data, show_list)
print(names)

movies_common_words = []

print("Most common words.")
for path in paths:
    print(path)
    movies_common_words.append(most_common_nouns(load_files_to_string(path, how_many=10), number_of_words))

movies_words_lists = []
sum_list = []
print("Words lists.")
for m in movies_common_words:
    word_list = [t[0] for t in m]
    movies_words_lists.append(word_list)
    sum_list += word_list

mean_vectors_list = []
print(len(names))
i = 1
print("Mean vectors.")
for name, m in zip(names, movies_words_lists):
    print(name)
    emb_dict = load_vectors(emb_dir + emb_file + '.vec', m)
    mean_vectors_list.append(mean_vectors(change_to_emb(m, emb_dict)))
    print(i)
    i += 1

df_vectors = pd.DataFrame({'show': names, 'vector': mean_vectors_list})

df_vectors.to_csv("emb_vectors_nouns.csv")



