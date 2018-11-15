import numpy as np
from typing import List


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
