FROM python:3.11

RUN https://huggingface.co/TheBloke/Llama-2-7B-GGUF/blob/main/llama-2-7b.Q5_K_M.gguf
RUN set FORCE_CMAKE=1 && set CMAKE_ARGS=-DLLAMA_CUBLAS=on
RUN python -m pip install -e . --force-reinstall --no-cache-dir
