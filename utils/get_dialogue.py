from langchain.prompts import PromptTemplate
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.output_parsers import JsonOutputParser


llm = LlamaCpp(
    # model_path="./models/llama-2-7b-chat.Q4_K_M.gguf",
    model_path="utils/models/llama-2-7b.Q5_K_M.gguf",
    temperature=0,
    max_tokens=4000,
    n_gpu_layers=32,
    n_batch=512,
    n_ctx=1024,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
    grammar_path="utils/assets/json.gbnf"
)

template = """
You task is to identify all the speakers and their dialogues from a given excerpt of a story. Categorize the sentences as either narration or dialogue. Assign dialogue to the identified speaker. If you cannot identify the speak call them Unknown. Return this data in the following JSON format.
{{
    "name": "speaker name",
    "text": "text spoken by speaker"
 }}

{text}
"""

prompt = PromptTemplate(template=template, input_variables=["text"])

dialogue_chain = prompt | llm | JsonOutputParser()



def get_dialogue(text: str):
    try:
        dialogue = dialogue_chain.invoke({"text": text})
        text = dialogue["text"]
        return text
    except Exception as e:
        print(e)
        return ""
