# from utils.get_dialogue import dialogue_chain
from utils.get_characters import Identifier, Splitter

TEXT = """
In the dimly lit tavern, the air thick with the scent of ale and the murmur of distant conversations, Captain Harlow and the elven rogue, Seraphina, huddled over a weathered map spread across their table. Harlow, his rugged face etched with the scars of countless battles, leaned in, his eyes narrowing as he traced a route with his calloused finger.

Harlow spoke with a gruff intensity, "The rumors point to these treacherous mountains, Seraphina. Our prize lies within the heart of the Forgotten Peaks, and we need every piece of information we can gather before setting foot in that perilous terrain."

Seraphina, her pointed ears twitching with anticipation, flicked a lock of silver hair from her eyes and countered, "Aye, Captain, but the locals here are a tight-lipped bunch. We need someone who knows more than what's spilled over a pint. Perhaps that hooded figure in the corner could be of assistance."

As they deliberated their next move, the tavern's raucous ambiance swirled around them, a medley of laughter and clinking tankards. The mysterious figure in the corner, cloaked in shadows, observed the duo with keen interest. Suddenly, a gravelly voice from the depths of the hood broke through, "Looking for secrets, are ye? Well, the Forgotten Peaks hold more than a few. But such knowledge comes at a cost." The duo exchanged a glance, acknowledging the impending twist in their quest.
"""
# response = dialogue_chain.invoke({"text": TEXT})
# print(response) 

identity = Identifier()
speakers = identity.get_speakers(text=TEXT)
print(speakers)

splitter = Splitter()
paragraphs = splitter.get_paragraphs(text=TEXT)
print(len(paragraphs))
print(paragraphs)
