## Curso ICMC aplicado aos dados de posicionamento político

> Brincando com os dados da IC para fazer umas coisinha;

# Importando e fazendo o download do Natural Language Toolkit 
import nltk
nltk.download()

# Abrindo o arquivo e tratando como string
# Primeiro com a notícia 07
with open("/content/Clean-noticia_007_Laura - noticia_007_Laura.txt", "r") as file:
    dados7 = file.read().replace('\n', '')

# Tokenização
stopwords = nltk.corpus.stopwords.words('portuguese')
nltk.word_tokenize(dados7)

# Usando Regex para Tratar o texto
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+')
tokens = tokenizer.tokenize(dados7)
print(tokens)

lista = []

for token in tokens:
  if token.lower() not in stopwords:
    lista.append(token.lower())

# Frequencia 
frequencia = nltk.FreqDist(lista)
frequencia.most_common()

# N - gramas

from nltk import bigrams
from nltk import trigrams
from nltk import ngrams

lista_bigrams = list(bigrams(lista))

lista_bigrams

# Trigramas #
lista_trigrams = list(trigrams(lista))

lista_trigrams

# N - gramas #
lista_ngrams = list(ngrams(lista, 4))

lista_ngrams

# Etiquetador #
from nltk.corpus  import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger

tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+')

etiq_padrao = DefaultTagger('N')

tokens = tokenizer.tokenize(dados7)

treinadoras = mac_morpho.tagged_sents()
etiquetador = UnigramTagger(treinadoras, backoff=etiq_padrao)

etiquetado = etiquetador.tag(tokens)

print(etiquetado)

# Chunking #

from nltk.chunk import RegexpParser

pattern = 'NP: {<NPROP><NPROP> | <N><N>}'
analise_gramatical = RegexpParser(pattern)
arvore =  analise_gramatical.parse(etiquetado)
print(arvore)

Notícia 15


> Mesmo processo, mas com a notícia *15*

# Abrindo o arquivo e tratando como string

with open("/content/Clean-noticia15.xlsx - noticia_015.txt", "r") as file:
    dados15 = file.read().replace('\n', '')

# Tokenização
stopwords = nltk.corpus.stopwords.words('portuguese')
nltk.word_tokenize(dados15)

# Usando Regex para Tratar o texto
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+')
tokens = tokenizer.tokenize(dados15)

# Minusculo e tirando stopwords portuguesas
lista = []

for token in tokens:
  if token.lower() not in stopwords:
    lista.append(token.lower())

# Frequencia 
frequencia = nltk.FreqDist(lista)
frequencia.most_common()

# N - gramas

from nltk import bigrams
from nltk import trigrams
from nltk import ngrams

lista_bigrams = list(bigrams(lista))

lista_bigrams

# Trigramas #
lista_trigrams = list(trigrams(lista))

lista_trigrams

# N - gramas #
lista_ngrams = list(ngrams(lista, 4))

lista_ngrams

# Etiquetador #
from nltk.corpus  import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger

tokenizer = RegexpTokenizer(r'[a-zA-Z]\w+')

etiq_padrao = DefaultTagger('N')

tokens = tokenizer.tokenize(dados15)

treinadoras = mac_morpho.tagged_sents()
etiquetador = UnigramTagger(treinadoras, backoff=etiq_padrao)

etiquetado = etiquetador.tag(tokens)

print(etiquetado)
