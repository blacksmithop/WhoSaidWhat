from re import sub


EXPR = r"(http\S+)|[^a-zA-Z0-9 -.?:;,()\"]"

def pre_proccess_text(text: str):
    text = text.replace("”", "\"")
    cleaned = sub(EXPR, "", text)
    return cleaned