# Analysing sentiment of movie reviews using Naive Bayes classifier

# Imports
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
reviews = ['This movie was fantastic! A must-watch.', 'I didn\'t enjoy this movie at all.', 'Amazing storyline and great acting!', 'The plot was dull and predictable.', 'Loved the cinematography! Highly recommended.', 'I would not recommend this movie to anyone.', 'An absolute masterpiece, truly inspiring.', 'Boring and too long, I almost fell asleep.', 'A thrilling experience from start to finish!', 'Not worth the time, very disappointing.']

labels = ['positive', 'negative', 'positive', 'negative', 'positive', 'negative', 'positive', 'negative', 'positive', 'negative']

# Text vectorization
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

# Splitting dataset
# x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

# Model training
model = MultinomialNB()
model.fit(x, labels)

# Test on new reviews instead of splitting dataset
new_reviews = ['What an incredible film! I was on the edge of my seat.', 'Totally boring, I walked out halfway through.']
x_test = vectorizer.transform(new_reviews)
y_test = ['positive', 'negative']

# Model evaluation
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

if accuracy > 0.8:
    print("Good vibes, this movie is worth watching!")
else:
    print("Eish, maybe skip this one.")