from utils import nearest_cos
import pandas as pd
import ast
import random


df = pd.read_csv('similarities.csv')
df = df.drop('Unnamed: 2', 1)
df = df.dropna(axis='rows')

df_top = df.iloc[:30, :]
print(df_top)

list_similiar = []

for index, row in df_top.iterrows():
    list_similiar.append(row['similatities'].split(','))


df_top['sim_list'] = list_similiar

# ready vectors
# df_comp1 = pd.read_csv('emb_vectors.csv')
# df_comp2 = pd.read_csv('emb_vectors_2.csv')
# df_comp3 = pd.read_csv('emb_vectors_3.csv')
# df_comp = pd.concat([df_comp1, df_comp2, df_comp3], ignore_index=True)
df_comp = pd.read_csv('emb_vectors_nouns.csv')
df_comp['ready_vector'] = [ast.literal_eval(vector) for vector in df_comp['vector']]
tuple_list = list(zip(df_comp['show'], df_comp['ready_vector']))
dict_show_vector = dict(zip(df_comp['show'], df_comp['ready_vector']))

print("All movies:" + str(len(tuple_list)))
ok = 0
for index, row in df_top.iterrows():
    if row['show'] not in dict_show_vector:
        continue
    print(row['show'] + ":")
    near_show = nearest_cos(dict_show_vector[row['show']], tuple_list, row['show'])
    print(near_show)
    if near_show in row['sim_list']:
        print("correct")
        ok += 1
    else:
        print("wrong")
    print("-------------------------------------")

print("Accuracy: " + str(ok/len(df_top.index)))

ok_random = 0
gone = 0
for index, row in df_top.iterrows():
    if row['show'] not in dict_show_vector:
        gone += 1
        continue
    tmp_list = list(df_comp['show'])
    tmp_list.remove(row['show'])
    near_show = random.choice(tmp_list)
    if near_show in row['sim_list']:
        ok_random += 1

print("Random accuracy: " + str(ok_random/len(df_top.index)))
print("Gone: " + str(gone))

