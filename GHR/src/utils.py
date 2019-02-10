import numpy as np
from typing import List, Tuple, Dict
import spacy
from collections import Counter
from scipy.stats.stats import pearsonr
nlp = spacy.load('en')


def similarity(v1: List[float], v2: List[float]) -> float:
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return float(np.dot(v1, v2) / n1 / n2)


def mean_vectors(vectors: List[List[float]]) -> List[float]:
    sum_vector = [0] * len(vectors[0])

    for v in vectors:
        sum_vector = [sum(x) for x in zip(sum_vector, v)]

    sum_vector = [el/len(vectors) for el in sum_vector]

    return sum_vector


# load embeddings for words
def change_to_emb(words: List[str], emb_dict: Dict) -> List[List[float]]:
    embs = []
    for word in words:
        if word in emb_dict:
            embs.append(emb_dict[word])

    return embs


def most_common_words(text: str, how_many: int) -> List:
    doc = nlp(text)
    # all tokens that arent stop words or punctuations
    words = [token.text for token in doc if
             token.is_stop != True and token.is_punct != True ] \
            # and (token.pos_ == "NOUN" or token.pos_ == "VERB" or token.pos_ == "ADJECTIVE")

    word_freq = Counter(words)
    common_words = word_freq.most_common(how_many)

    return common_words


def most_common_nouns(text: str, how_many: int) -> List:
    doc = nlp(text)
    # noun tokens that arent stop words or punctuations
    nouns = [token.text for token in doc if
             token.is_stop != True and token.is_punct != True and (token.pos_ == "NOUN")]

    noun_freq = Counter(nouns)
    common_nouns = noun_freq.most_common(how_many)

    return common_nouns


def create_bag_of_words(doc_words: List[Tuple[str, int]], all_words: List[str]) -> List[int]:
    bag_of_words = [0]*len(all_words)

    for i, w in enumerate(all_words):
        for t in doc_words:
            if w == t[0]:
                bag_of_words[i] = t[1]

    return bag_of_words


# finding nearest embedding by cosine similarity
def nearest_cos(vector: List, all_vectors: List[Tuple[str,List]], target_name: str) -> str:
    max = 0
    max_str = ""
    for name, vec in all_vectors:
        sim = similarity(vector, vec)
        if target_name != name and sim > max:
            max = sim
            max_str = name

    return max_str


# finding nearest embedding by correlation
def nearest_corr(vector: List[int], all_vectors: List[Tuple[str,List[int]]], target_name: str) -> str:
    max = 0
    max_str = ""
    for name, vec in all_vectors:
        sim = pearsonr(vector, vec)[0]
        if target_name != name and sim > max:
            max = sim
            max_str = name

    return max_str


