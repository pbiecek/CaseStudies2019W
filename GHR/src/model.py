from torch import nn
import torch
from torch.autograd import Variable
from torch import Tensor


class LSTMEmbeddings(nn.Module):

    def __init__(self, embedding_dim: int, hidden_dim: int, vocab_size: int, sentence_length: int, word_embeddings: nn.Embedding = None):
        super(LSTMEmbeddings, self).__init__()
        self.sentence_length = sentence_length
        self.hidden_dim = hidden_dim
        if word_embeddings is None:
            self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)
        else:
            self.word_embeddings = word_embeddings

        self.lstm = nn.LSTM(embedding_dim, hidden_dim)

        self.hidden = self.init_hidden()

    def init_hidden(self):
        return (torch.zeros(1, 1, self.hidden_dim),
                torch.zeros(1, 1, self.hidden_dim))

    def forward(self, input: Variable)-> Tensor:
        self.hidden = self.init_hidden()
        embeds = self.word_embeddings(input)
        lstm_out, (self.hidden, _) = self.lstm(embeds.view(self.sentence_length, 1, 300), self.hidden)

        return self.hidden


