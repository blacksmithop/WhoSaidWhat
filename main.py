from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.output_parsers import JsonOutputParser


# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    # model_path="./models/llama-2-7b-chat.Q4_K_M.gguf",
    model_path="./models/llama-2-7b.Q5_K_M.gguf",
    temperature=0,
    max_tokens=4000,
    n_gpu_layers=32,
    n_batch=512,
    n_ctx=1024,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
    grammar_path="./json.gbnf"
)

template = """
<s>[INST] <<SYS>>
You task is to identify all the speakers and their dialogues from a given excerpt of a story. Categorize the sentences as either narration or dialogue. Assign each dialogue to a speaker identified, if you cannot identify the speak name them "Unknown". Return this data in the following JSON format.
[
    {{
        [
            {{
                "name": "speaker name",
                "text": "text spoken by speaker"
            }},
            ...
        ]
    }}
]
<</SYS>>
{text}
"""

prompt = PromptTemplate(template=template, input_variables=["text"])

chain = prompt | llm | JsonOutputParser()

TEXT = """
In the dimly lit tavern, the air thick with the scent of ale and the murmur of distant conversations, Captain Harlow and the elven rogue, Seraphina, huddled over a weathered map spread across their table. Harlow, his rugged face etched with the scars of countless battles, leaned in, his eyes narrowing as he traced a route with his calloused finger.

Harlow spoke with a gruff intensity, "The rumors point to these treacherous mountains, Seraphina. Our prize lies within the heart of the Forgotten Peaks, and we need every piece of information we can gather before setting foot in that perilous terrain."

Seraphina, her pointed ears twitching with anticipation, flicked a lock of silver hair from her eyes and countered, "Aye, Captain, but the locals here are a tight-lipped bunch. We need someone who knows more than what's spilled over a pint. Perhaps that hooded figure in the corner could be of assistance."

As they deliberated their next move, the tavern's raucous ambiance swirled around them, a medley of laughter and clinking tankards. The mysterious figure in the corner, cloaked in shadows, observed the duo with keen interest. Suddenly, a gravelly voice from the depths of the hood broke through, "Looking for secrets, are ye? Well, the Forgotten Peaks hold more than a few. But such knowledge comes at a cost." The duo exchanged a glance, acknowledging the impending twist in their quest.
"""
response = chain.invoke({"text": TEXT})
print(response)


