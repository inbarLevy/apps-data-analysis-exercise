from DataAnalysis import Intro
import matplotlib.pyplot as plt
import numpy as np

apps = Intro.apps
user_reviews = Intro.user_reviews

# Count of total items by Sentiment
count_sentiment = user_reviews.groupby('Sentiment')['Sentiment'].aggregate(lambda x: x.count())
count_sentiment.plot.bar(rot=1, fontsize=10, width=0.6, colormap='Blues_r')
plt.xlabel('Sentiment', fontsize=13, fontname='Lucida Sans Unicode')
plt.ylabel('Number of items', fontsize=13, fontname='Lucida Sans Unicode')
plt.title('Count of total items by Sentiment', fontsize=20, fontname='Lucida Sans Unicode')
plt.show()

# Average rating by genres
single_genres = apps[apps['Genres'].str.contains('[;]', na=False) == False][['Genres', 'Rating']]
multi_genres = apps[apps['Genres'].str.contains('[;]', na=False)][['Genres', 'Rating']]
for row in multi_genres.iterrows():
    rating = row[1]['Rating']
    genres = row[1]['Genres']
    for genre in genres.split(';'):
        single_genres = single_genres.append({'Genres': genre, 'Rating': rating}, ignore_index=True)
avg_rating = single_genres.groupby('Genres')['Rating'].aggregate(np.mean).dropna()
avg_rating.plot.bar(fontsize=9, rot=90, colormap='Accent_r', figsize=(3, 2.8), include_bool=True)
plt.xlabel('Genres', fontsize=16, fontname='Lucida Sans Unicode')
plt.ylabel('Average rating', fontsize=16, fontname='Lucida Sans Unicode')
plt.title('Average rating by genres', fontsize=20, fontname='Lucida Sans Unicode')
plt.show()

# Polarity difference between Free apps and Paid apps
type_Polarity = apps[['App', 'Type']].join(user_reviews[['App', 'Sentiment_Polarity']].set_index('App'),
                                           on='App').dropna()
type_Polarity.boxplot(by='Type', column='Sentiment_Polarity', widths=0.5, fontsize=15)
plt.xlabel('Sentiment_Polarity', fontsize=16, fontname='Lucida Sans Unicode')
plt.title('Polarity difference between Free apps and Paid apps', fontsize=20, fontname='Lucida Sans Unicode')
plt.suptitle('')
plt.show()

# Statistical measures by app Category
category_rating_measures = apps.groupby('Category')['Rating'].aggregate(
    [np.mean, np.std, np.median, lambda x: x.mode()]).dropna()
category_rating_measures.plot.bar(use_index=False)
plt.xlabel('Category', fontsize=16, fontname='Lucida Sans Unicode')
plt.title('Statistical measures by app Category', fontsize=20, fontname='Lucida Sans Unicode')
plt.show()

# the average and the mean of EDUCATION are the same, and the STD is minimal, and the mode is close to the average
# and mean value, that is why it is the most stable category
