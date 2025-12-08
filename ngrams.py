# Imports
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Tokenisation using NLTK
sample_text = "I love programming, and I enjoy learning new languages."
tokens = word_tokenize(sample_text)

# Ngram generation using NLTK
unigrams = list(ngrams(tokens, 1))
bigrams = list(ngrams(tokens, 2))
trigrams = list(ngrams(tokens, 3))

print("Unigrams:", unigrams)
print("\n")
print("Bigrams:", bigrams)
print("\n")
print("Trigrams:", trigrams)