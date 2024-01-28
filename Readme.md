# Dynamic Narrator

## Installation

1. Get [https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q5_K_M.gguf](https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q5_K_M.gguf)

2. Install llama-cpp-python with GPU support

3. Install dependencies


### Challenges:

- [ ] Model hallucinates, 
> For instance when given excerpts from Love & Prejudice it fills in missing characters and text.

- [ ] Model is identified by llama-2 but not by spacy
  - [ ] Extract speakers by model (longer input, lcel chains etc.)