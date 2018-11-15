import io
from vocab import Vocab
from vocab import build_vocab
from numpy import array
import pandas as pd
from sklearn.model_selection import train_test_split


def load_file(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    lines = []
    for line in fin:
        lines.append(line)
    return lines


def load_file_to_string(fname: str) -> str:
    with open(fname, 'r') as myfile:
        data = myfile.read().replace('\n', '')
    return data


def load_data_to_one_str(fname, vocab, max_len):
    doc = load_file_to_string(fname)

    tokens = doc.rstrip().split(' ')
    encoded_doc = []
    i = 1
    for token in tokens:
        if i == max_len:
            break
    encoded_doc.append(vocab.get_index(token))
    i += 1

    for i in range(0, max_len - len(encoded_doc)):
        encoded_doc.append(0)

    for i in range(0, len(encoded_doc)):
        if encoded_doc[i] is None:
            encoded_doc[i] = 0

    return encoded_doc


def load_data(fname, vocab, max_len):
    docs = load_file(fname)
    encoded_docs = []

    for doc in docs:
        tokens = doc.rstrip().split(' ')
        encoded_doc = []
        i = 1
        for token in tokens:
            if i == max_len:
                break
            encoded_doc.append(vocab.get_index(token))
            i += 1
        encoded_docs.append(encoded_doc)

    for doc in encoded_docs:
        for i in range(0, max_len - len(doc)):
            doc.append(0)

    for doc in encoded_docs:
        for i in range(0, len(doc)):
            if doc[i] is None:
                doc[i] = 0

    return encoded_docs
