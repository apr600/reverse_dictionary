
# NLTK Imports
import nltk
from nltk.corpus import wordnet as wn


syns = wn.synsets("good")
print(syns[0].name())

synonyms = []
antonyms = []
for syn in syns:
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("synonyms: ", set(synonyms))
print("antonyms: ", set(antonyms))
