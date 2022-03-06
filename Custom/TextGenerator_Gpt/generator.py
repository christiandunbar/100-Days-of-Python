import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

#sequence = ("He began his premiership by forming a five-man war cabinet which included Chamberlain as Lord President of the Council, Labour leader Clement Attlee as Lord Privy Seal (later as Deputy Prime Minister), Halifax as Foreign Secretary and Labour's Arthur Greenwood as a minister without portfolio. In practice,")
sequence = ("I'm current studying Python programmming. It's super exciting stuff and I can't wait to be able to")

inputs = tokenizer.encode(sequence, return_tensors='pt')
outputs = model.generate(inputs, max_length=200, do_sample=True, temperature=.7, top_k=50)

text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)

