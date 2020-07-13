import pandas as pd
import dateparser

try:
    # change
    user_reviews = pd.read_csv('./DataFiles/reviews.csv')
    review_num_of_rows = user_reviews.shape[0]
except:
    print('Error while handling user_reviews file.')

try:
    # change
    apps = pd.read_csv('./DataFiles/apps.csv', parse_dates=["Last Updated"], date_parser=lambda x: dateparser.parse(x))
    apps_num_of_rows = apps.shape[0]
except:
    print('Error while handling apps file.')

try:
    if __name__ == '__main__':
        print('user_reviews table:')
        print('Number of rows: ', review_num_of_rows)
        print('Columns names: ', list(user_reviews.columns))
        print('\napps table:')
        print('Number of rows: ', apps_num_of_rows)
        print('Columns names: ', list(apps.columns))

        # number of categories
        apps_categories_count = apps['Category'].drop_duplicates().size
        print('\nTotal count of apps categories: {}'.format(apps_categories_count))

        # heaviest app
        max_size = apps[apps['Size'].str.contains('M$', na=False)]['Size'].max()
        heaviest_app = apps[apps['Size'] == max_size]['App'].drop_duplicates().values
        print('\nThe heaviest apps: {}'.format(heaviest_app))

        # most installations
        max_installs = apps['Installs'].max()
        most_installed_app = apps[apps['Installs'] == max_installs]['App'].drop_duplicates().values
        print('\nThe apps with most installations: {}'.format(most_installed_app))

        # most updated
        max_update_date = apps['Last Updated'].max()
        updated_app = apps[apps['Last Updated'] == max_update_date]['App'].drop_duplicates().values
        print('\nThe most updated apps: {}'.format(updated_app))

        # most popular app genres
        most_popular_app = apps[apps['Installs'] == apps['Installs'].max()][
            ['App', 'Rating', 'Genres']].drop_duplicates()
        most_popular_app_max_rating = most_popular_app['Rating'].max()
        most_popular_app_genre = most_popular_app[most_popular_app['Rating'] == most_popular_app_max_rating][
            'Genres'].drop_duplicates()
        print('\nThe most popular app\'s genres: {}'.format(most_popular_app_genre.values))
except:
    print('Error while handling apps file.')

# The tables has no PK or Fk, because they don't have a unique values. we understand that the column 'App' in user_reviwe
# should be a Fk, but in reality there are apps in user_review which does not exist in apps table.
