import pandas as pd
import numpy as np
import csv

data = pd.read_csv("datanot1718.csv")

# Get Actor Features

# TODO

most_pop_actor = np.array([(name, freq) for freq, name in sorted(zip(freqs, names), reverse=True)])[:12]
print("Top 12:", most_pop_actor)

print()

# Get Director Features

# TODO

most_pop_director = np.array([[name, freq] for freq, name in sorted(zip(freqs, names), reverse=True)])[:5]
print("Top 5:", most_pop_director)

print()

# Get Genres Features

# TODO

all_genres = np.array([[name, freq] for freq, name in sorted(zip(freqs, names), reverse=True)])
print("All Genres:", all_genres)

print()

# Get All Features
features = np.array([])
features = np.concatenate([features, all_genres[:,0], most_pop_director[:,0], most_pop_actor[:,0]])
print("Features:",features,"Length:",len(features))