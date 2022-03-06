import torch
from torch.utils.data import Dataset


class MovieDataset(Dataset):
    def __init__(self, tokenizer_scoped, init_token, movie_titles, max_len, extra_length):
        self.max_len = max_len
        self.extra_length = extra_length
        self.tokenizer = tokenizer_scoped
        self.eos = self.tokenizer.eos_token
        self.eos_id = self.tokenizer.eos_token_id
        self.movies = movie_titles
        self.result = []

        for movie in self.movies:
            # Encode the text using tokenizer.encode(). We assess EOS at the end
            tokenized = self.tokenizer.encode(init_token + movie + self.eos)

            # Padding/truncating the encoded sequence to max_len
            padded = self.pad_truncate(tokenized)

            # Creating a tensor and adding to the result
            self.result.append(torch.tensor(padded))

    def __len__(self):
        return len(self.result)

    def __getitem__(self, item):
        return self.result[item]

    def pad_truncate(self, name):
        name_length = len(name) - self.extra_length
        if name_length < self.max_len:
            difference = self.max_len - name_length
            result = name + [self.eos_id] * difference
        elif name_length > self.max_len:
            result = name[:self.max_len + 2] + [self.eos_id]
        else:
            result = name
        return result
