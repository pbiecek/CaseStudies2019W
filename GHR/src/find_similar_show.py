from utils import nearest_cos
import pandas as pd
import ast

# Load document embeddings
df_comp = pd.read_csv('emb_vectors_nouns.csv')
df_comp['ready_vector'] = [ast.literal_eval(vector) for vector in df_comp['vector']]
tuple_list = list(zip(df_comp['show'], df_comp['ready_vector']))
dict_show_vector = dict(zip(df_comp['show'], df_comp['ready_vector']))

# For every show find the most similar show
print("All movies:" + str(len(tuple_list)))
ok = 0
for index, row in df_comp.iterrows():
    if row['show'] not in dict_show_vector:
        continue
    print(row['show'] + ":")
    near_show = nearest_cos(dict_show_vector[row['show']], tuple_list, row['show'])
    print(near_show)
    print("-------------------------------------")

