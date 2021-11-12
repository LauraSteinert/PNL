# Importing NLTK #
import nltk
nltk.download()

# Checking the length of the corpus and the sentences on it #
len(nltk.corpus.mac_morpho.words())
nltk.corpus.mac_morpho.sents()

# Test tokenizer #
texto = "O jogador é um palerma, obviamente"
nltk.word_tokenize(texto)

# Importing Regex Tokenizer #
from nltk.tokenize import RegexpTokenizer

texto = "Running away is easy, 1s the living thaats haard"
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(texto)
print(tokens)

# Regex improved #
tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+')
tokens = tokenizer.tokenize(texto)
print(tokens)

# Frequency #
frequencia = nltk.FreqDist(tokens)
frequencia.most_common()

# Everything in lower char #
nova_lista = []
for token in tokens:
  nova_lista.append(token.lower())
frequencia = nltk.FreqDist(nova_lista)
frequencia.most_common()

#Stopwords#

stopwords = ntlk.corpus.stopwords.words('portuguese')

# Tokenizing again - TODO #

lista = []

for token in tokens:
  if token.lower() not in stopwords:
    lista.append(token.lower())

# Frequency again - TODO #

# N - grams # 
texto = nltk.corpus.mac_morpho.sents()
stopwords = nltk.corpus.stopwords.words('portuguese')

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'[a-zA-z]\w+')
tokens = tokenizer.tokenize(str(texto))

lista = []
for token in tokens:
  if token.lower() not in stopwords:
    lista.append(token.lower())
print(lista)

frequencia = nltk.FreqDist(lista)

# N - grams #
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams

lista_bigrams = list(bigrams(lista))

lista_bigrams

# Trigrams #
lista_trigrams = list(trigrams(lista))

lista_trigrams

# N - grams #
lista_ngrams = list(ngrams(lista, 4))

lista_ngrams

for bigrama in lista_bigrams:
  print(bigrama[0][0])
  
# Stemming e Lematizing #

stemmer = nltk.RSLPStemmer()

print(stemmer.stem("amigão"))
print(stemmer.stem("amigos"))
print(stemmer.stem("amigo"))
print(stemmer.stem("propõem"))
print(stemmer.stem("propuseram"))
print(stemmer.stem("propondo"))


# Tagging #
from nltk.corpus  import mac_morpho
from nltk.tag import UnigramTagger


tokens = nltk.word_tokenize(corpus)

treinadoras_natacao = mac_morpho.tagged_sents()
etiquetador = UnigramTagger(treinadoras_natacao)

etiquetado = etiquetador.tag(tokens)

print(etiquetado)

# Same thing, but now with an default tagger #

from nltk.corpus  import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger

tokens = nltk.word_tokenize(corpus)

etiq_padrao = DefaultTagger('N')
treinadoras_natacao = mac_morpho.tagged_sents()
etiquetador = UnigramTagger(treinadoras_natacao, backoff=etiq_padrao)

etiquetado = etiquetador.tag(tokens)

print(etiquetado)

# Chunking #

from nltk.chunk import RegexpParser

pattern = 'NP: {<NPROP><NPROP> | <N><N>}'
analise_gramatical = RegexpParser(pattern)
arvore =  analise_gramatical.parse(etiquetador)
