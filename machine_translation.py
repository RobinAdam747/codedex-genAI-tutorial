# Imports
from translate import Translator

# Create translator object
translator = Translator(to_lang='nl')  # Dutch

# Choose and translate text
text = "Hello, how are you?"

translation = translator.translate(text)
print("Original Text:", text)
print("Translated Text:", translation)