import io
import os
from typing import List, Dict


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


def load_files_to_string(path: str) -> str:
    all_data = ""
    for fname in os.listdir(path):
        with open(path + "/" + fname, 'r') as myfile:
            data = myfile.read().replace('\n', '')
            all_data += data
    return all_data


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


def vector(line):
    """ Line is in the format output by print-sentence-vector """
    v = line.split()[-300:]
    return list(map(float, v))


def load_vectors(fname: str, list: List[str]) -> Dict:
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in fin:
        tokens = line.rstrip().split(' ')
        if tokens[0] in list:
            data[tokens[0]] = vector(line)
    return data

