from DataAnalysis import Intro
import numpy as np
import pandas as pd

apps = Intro.apps
user_reviews = Intro.user_reviews

num_of_positive = user_reviews[user_reviews['Sentiment'] == 'Positive']['App'].count()
print('The number of apps classified as Positive sentiment: {}'.format(num_of_positive))

num_of_neutral = user_reviews[user_reviews['Sentiment'] == 'Neutral']['App'].count()
print('\nThe number of apps classified as Neutral sentiment: {}'.format(num_of_neutral))

num_of_negative = user_reviews[user_reviews['Sentiment'] == 'Negative']['App'].count()
print('\nThe number of apps classified as Negative sentiment: {}'.format(num_of_negative))

top20_reviewed_apps = apps[['App', 'Reviews', 'Rating']].nlargest(20, 'Reviews')
top_rated = top20_reviewed_apps[top20_reviewed_apps['Rating'] == top20_reviewed_apps['Rating'].max()]
top_app_sentiments = pd.merge(top_rated, user_reviews[['App', 'Sentiment']], on='App', how='inner')
top_app_sentiments.set_index('App', inplace=True)
if top_app_sentiments.empty:
    print('\nThe most rated app has no sentiment')
else:
    print('\nThe sentiment of the most rated app:{} '.format(top_app_sentiments))

x = user_reviews[['App', 'Sentiment_Polarity']]
y = apps[apps['Type'] == 'Free']['App']
z = pd.merge(x, y, on='App', how='inner')
z.set_index('App', inplace=True)
print('\nThe average polarity of free apps is {}'.format(z['Sentiment_Polarity'].mean()))


def get_average_polarity(app_name):
    try:
        return user_reviews[user_reviews['App'] == app_name].groupby('App')['Sentiment_Polarity'].aggregate(
            np.mean).values
    except:
        print('Error while handling' + app_name)
        return


def get_sentiment(app_name):
    app_reviews = get_average_polarity(app_name)
    if 1 > app_reviews > 0.1:
        print(app_name + "'s reviews are most Positive")
        return
    if -1 < app_reviews < -0.1:
        print(app_name + "'s reviews are most Negative")
        return
    print(app_name + "'s reviews are most Neutral")
    return

