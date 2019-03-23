import pandas as pd
import numpy as np
import csv

data = pd.read_csv("datanot1718.csv")

# Get Actor Features
actor_list = "|".join(data["actors"].values)
actor_list = actor_list.split("|")
names, freqs = np.unique(actor_list, return_counts=True)
print("Total Unique Saved Actor:",len(names))

most_pop_actor = np.array([(name, freq) for freq, name in sorted(zip(freqs, names), reverse=True)])[:12]
print("Top 12:", most_pop_actor)

print()

# Get Director Features
director_list = "|".join(data["directors"].values)
director_list = director_list.split("|")
names, freqs = np.unique(director_list, return_counts=True)
print("Total Unique Saved Director:",len(names))

most_pop_director = np.array([[name, freq] for freq, name in sorted(zip(freqs, names), reverse=True)])[:5]
print("Top 5:", most_pop_director)

print()

# Get Genres Features
genre_list = "|".join(data["genres"].values)
genre_list = genre_list.split("|")
names, freqs = np.unique(genre_list, return_counts=True)
print("Total Unique Saved Genres:",len(names))

all_genres = np.array([[name, freq] for freq, name in sorted(zip(freqs, names), reverse=True)])
print("All Genres:", all_genres)

print()

# Get All Features
features = np.array([])
features = np.concatenate([features, all_genres[:,0], most_pop_director[:,0], most_pop_actor[:,0]])
print("Features:",features,"Length:",len(features))

