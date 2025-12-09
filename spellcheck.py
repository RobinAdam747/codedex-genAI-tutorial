# Imports
from textblob import TextBlob

# Incorrect text
incorrect_text = "I hav a speling eror in this sentense."

# Spell checking and correction
blob = TextBlob(incorrect_text)
corrected_text = blob.correct()

# Output results
print("Original Text:", incorrect_text)
print("Corrected Text:", corrected_text)