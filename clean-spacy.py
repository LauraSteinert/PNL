pip install -U spacy
pip install -U spacy-lookups-data
!python -m spacy download pt_core_news_lg
import spacy

texto = "A bananinha, que bonita, a bananinha. A mais bela bananinha do mundo"
nlp = spacy.load("pt_core_news_lg")
doc = nlp(texto)

tokens = [token .orth_ for token in doc]
tokens
