import pandas as pd
import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModelWithLMHead
import torch.optim as optim
from os.path import exists
from utils.dataset_utils import MovieDataset
from utils.model_utils import train, model_infer

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.encode("movie: ")
model = AutoModelWithLMHead.from_pretrained("gpt2")
model = model.to(device)


def get_movie_list():
    movies_file = "movies.csv"
    raw_df = pd.read_csv(movies_file, low_memory=False)
    return raw_df.original_title


movie_list = get_movie_list()
trained_model_exists = exists("movie_gpt.pth")


if trained_model_exists:
    model.load_state_dict(torch.load("movie_gpt.pth"))
else:
    print(f"Rows in training data: {len(movie_list)}")
    avg_length = sum([len(name.split()) for name in movie_list]) / len(movie_list)
    max_length = 10
    optimizer = optim.AdamW(model.parameters(), lr=3e-4)
    extra_length = len(tokenizer.encode("movie: "))

    dataset = MovieDataset(tokenizer, "movie: ", movie_list, max_length, extra_length)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True, drop_last=True)
    train(model=model, optimizer=optimizer, dl=dataloader, epochs=2, device=device)
    torch.save(model.state_dict(), "movie_gpt.pth")

results = set()
while len(results) < 20:
    name = model_infer(model, tokenizer, "movie:", device).replace("movie: ", "").strip()
    if name.isascii() and name not in set(movie_list) and name not in results:
        results.add(name)
        print(name)
