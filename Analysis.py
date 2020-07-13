import Intro
import re
import pandas as pd

apps = Intro.apps

# genres_count
series_of_single_genres = apps[apps['Genres'].str.contains('[;]', na=False) == False]['Genres']
series_of_multi_genres = apps[apps['Genres'].str.contains('[;]', na=False)]['Genres']
for genres in series_of_multi_genres:
    series_of_single_genres = series_of_single_genres.append(pd.Series(re.split('[;]', genres)))
genres_count = series_of_single_genres.value_counts()
print('The  number of apps by genres:\n {}'.format(genres_count))

# list of free apps
print("\nlist of free apps:\n{}".format(apps[apps['Type'] == 'Free']['App'].drop_duplicates()))


def get_app_details_by_letter(letter):
    return apps[apps['App'].str.startswith(letter)]


# Popular type
type_counts = apps['Type'].value_counts()
print("\nThere are {} {} apps and {} {} apps, so the most popular is {}.".format(type_counts[0], type_counts.index[0],
                                                                               type_counts[1], type_counts.index[1],
                                                                               type_counts.index[0]))
