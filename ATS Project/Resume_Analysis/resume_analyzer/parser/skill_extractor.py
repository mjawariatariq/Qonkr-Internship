# skill_extractor file
import spacy
# Ye line spaCy ke andar se EntityRuler naam ka tool uthati hai, jisse hum apne khud ke rules define kar sakte hain, jaise "Python" ko skill samajhna.
from spacy.pipeline import EntityRuler
from parser.skill_extractor import get_skills, unique_skills

# Ye line ek powerful English NLP model load karti hai jo already trained hai aur English ke lafzon ko achay se samajhta hai.
nlp = spacy.load("en_core_web_sm")

# Hum entity_ruler NLP pipeline mein daal rahay hain, taake hum apne rules use kar saken — jaise har resume mein "Data Science" ko SKILL mana jaye.
ruler = nlp.add_pipe("entity_ruler")

# Yeh file mein likhay huay patterns (skills waghera) ko load karta hai. SpaCy in patterns ko use karke resume mein skills identify karega.
# This line loads a previously saved file that contains your custom skill patterns for entity recognition.
ruler.from_disk("jz_skill_patterns.jsonl")

# Adding the entity ruler to the NLP pipeline again (redundant in this case)
# If you want to add custom rules more than once, be mindful to avoid duplicate declarations.
# ruler = nlp.add_pipe("entity_ruler")


def get_skills(text):
    doc = nlp(text)
    
    # subset stores skills from the current text
    subset = []
    for ent in doc.ents:
        if ent.label_ == "SKILLS":  # Ensure 'label_' is used to check the label
            subset.append(ent.text)  # If it's a skill, add it to the subset list.
    
    # Finally, return the list of extracted skills.
    return subset

# any duplicate entries in the original list will be removed automatically when converted into a set.
# Remove duplicates from a list of skills, returning only unique skills.
def unique_skills(x):
    return list(set(x))
