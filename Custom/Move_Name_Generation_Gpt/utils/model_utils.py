import torch
import numpy as np


def train(model, optimizer, dl, epochs, device):
    for epoch in range(epochs):
        for idx, batch in enumerate(dl):
            with torch.set_grad_enabled(True):
                optimizer.zero_grad()
                batch = batch.to(device)
                output = model(batch, labels=batch)
                loss = output[0]
                loss.backward()
                optimizer.step()
                if idx % 50 == 0:
                    print(f"loss: {loss}, {idx}")


def topk(probs, n=9):
    # The scores are initially softmaxed to convert to probabilities
    probs = torch.softmax(probs, dim=-1)

    # PyTorch has its own topk method, which we use here
    tokensProb, topIx = torch.topk(probs, k=n)

    # The new selection pool (9 choices) is normalized
    tokensProb = tokensProb / torch.sum(tokensProb)

    # Send to CPU for numpy handling
    tokensProb = tokensProb.cpu().detach().numpy()

    # Make a random choice from the pool based on the new prob distribution
    choice = np.random.choice(n, 1, p=tokensProb)
    tokenId = topIx[choice][0]

    return int(tokenId)


def model_infer(model, tokenizer, init_token, device, max_length=10):
    # Preprocess the init token (task designator)
    init_id = tokenizer.encode(init_token)
    result = init_id
    init_input = torch.tensor(init_id).unsqueeze(0).to(device)

    with torch.set_grad_enabled(False):
        # Feed the init token to the model
        output = model(init_input)

        # Flatten the logits at the final time step
        logits = output.logits[0, -1]

        # Make a top-k choice and append to the result
        result.append(topk(logits))

        # For max_length times:
        for i in range(max_length):
            # Feed the current sequence to the model and make a choice
            input = torch.tensor(result).unsqueeze(0).to(device)
            output = model(input)
            logits = output.logits[0, -1]
            res_id = topk(logits)

            # If the chosen token is EOS, return the result
            if res_id == tokenizer.eos_token_id:
                return tokenizer.decode(result)
            else:  # Append to the sequence
                result.append(res_id)
    # IF no EOS is generated, return after the max_len
    return tokenizer.decode(result)