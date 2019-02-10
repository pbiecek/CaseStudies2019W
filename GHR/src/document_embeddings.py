from utils import most_common_words, most_common_nouns, create_bag_of_words, similarity, nearest_cos, \
    change_to_emb, mean_vectors
from files import load_data, load_file_to_string, load_files_to_string, load_vectors, load_paths_from_dir
import pandas as pd

# Settings
data = 'data/shows'
number_of_words = 100
max_len = 20000
emb_dir = 'embedding/'
emb_file = 'wiki.en'

# Load names and paths of shows from chosen directory
names, paths = load_paths_from_dir(data)
print(names)


# Choose most common nouns from shows subtitles
movies_common_words = []
print("Most common words.")
for path in paths:
    print(path)
    movies_common_words.append(most_common_nouns(load_files_to_string(path, how_many=10), number_of_words))

# Make lists of most common nouns
movies_words_lists = []
sum_list = []
print("Words lists.")
for m in movies_common_words:
    word_list = [t[0] for t in m]
    movies_words_lists.append(word_list)
    sum_list += word_list

# Create  embeddings for documents
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



