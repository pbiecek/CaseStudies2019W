from embeddings import load_embedding_model
from vocab import Vocab, build_vocab
from model import LSTMEmbeddings
from dataset import load_data, load_data_to_one_str
import torch
from torch.autograd import Variable
from utils import similarity, mean_vectors
from torch.nn import Embedding

data = 'data'
emb_dir = 'embedding/'
emb_file = 'wiki.pl'
embedding_dim = 300
hidden_dim = 50
sentence_length = 8

vocab_file = 'tmp/vocab.txt'
build_vocab([
        emb_dir+emb_file+'.vec'
    ], 'tmp/vocab.txt')
vocab = Vocab(filename=vocab_file)
emb: Embedding = load_embedding_model(data=data, emb_dir=emb_dir, emb_file=emb_file, vocab=vocab, input_dim=embedding_dim)
model = LSTMEmbeddings(embedding_dim, hidden_dim, vocab.size(), sentence_length, emb)

encoded_file_animals = load_data(data+"/animals.txt", vocab, sentence_length)
encoded_file_buildings = load_data(data+"/buildings.txt", vocab, sentence_length)

# encoded_file_batman_beyond = \
#     load_data_to_one_str(data+"/shows/Batman Beyond/batman_beyond_-_1x01_-_rebirth_-_part_1_.vpc.txt", vocab, sentence_length)
#
# encoded_file_batman_animated = \
#     load_data_to_one_str(data + "/shows/Batman: The Animated Series/01. On Leather Wings.txt", vocab, sentence_length)

# encoded_file_dharma_greg = \
#     load_data_to_one_str(data + "/shows/Dharma__Greg_01x01_Pilot_en_23.976fps_-Fov.txt", vocab, sentence_length)

# first = [encoded_file_batman_beyond]
# second = [encoded_file_batman_animated]
# third = [encoded_file_dharma_greg]

first = [encoded_file_animals[8]]
second = [encoded_file_animals[9]]
third = [encoded_file_buildings[0]]

first = Variable(torch.LongTensor(first))
second = Variable(torch.LongTensor(second))
third = Variable(torch.LongTensor(third))

first_emb = mean_vectors(emb(first).data.numpy()[0])
second_emb = mean_vectors(emb(second).data.numpy()[0])
third_emb = mean_vectors(emb(third).data.numpy()[0])

output1 = model(first)
output2 = model(second)
output3 = model(third)

v1 = output1.data.numpy()[0][0]
v2 = output2.data.numpy()[0][0]
v3 = output3.data.numpy()[0][0]

print(first_emb)
print(second_emb)
print(third_emb)


print(similarity(v1, v2))
print(similarity(v2, v3))

print(similarity(first_emb, second_emb))
print(similarity(second_emb, third_emb))
