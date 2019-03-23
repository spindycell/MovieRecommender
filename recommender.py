import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

features = ["Comedy","Drama","Action","Romance","Adventure","Thriller","Crime","Fantasy","Children","Animation","Sci-Fi","Horror","Mystery","IMAX","Musical","Documentary","War","Western","(no genres listed)",
            "Todd Phillips","Dennis Dugan","Peter Farrelly","Jay Roach","Frank Coraci",
            "Adam Sandler","Will Ferrell","Johnny Depp","Jim Carrey","Vince Vaughn","Ben Stiller","Robert De Niro","Paul Rudd","Jennifer Aniston","Jack Black","Drew Barrymore","Cameron Diaz"]

data = pd.read_csv("datanot1718.csv")
datatest = pd.read_csv("data1718.csv")
data["userRating"] = pd.to_numeric(data["userRating"])

# Reformat data menjadi Table Fitur
def reformat(data, features):
    for i,f in enumerate(features):
        data[f] = 0.0
        for index, row in data.iterrows():
            if i < 19:
                if f in row["genres"]:
                    data.loc[index, f] = 1.0
            elif i < 23:
                if f in row["directors"]:
                    data.loc[index, f] = 0.2
            elif i < 35:
                if f in row["actors"]:
                    data.loc[index, f] = 0.3
    data = data.drop(["title","userId","imdbRating","genres","directors","actors"],axis=1)
    return data

data = reformat(data, features)
datatest = reformat(datatest, features)

# Mengalikan Bobot Fitur dengan User Rating
for f in features:
    data[f] *= data["userRating"]

data.to_csv("fitur_item.csv", sep=',',encoding='utf-8', index=False)

# Mendapatkan User Profile
user_profile = data.loc[:,"Comedy":].sum(axis=0)                     
user_profile = user_profile / user_profile.sum()
print(user_profile)                        

# Scoring
datatest["value"] = 0.0
for index, row in datatest.iterrows():
    datatest.loc[index, "value"]=(datatest.loc[index,"Comedy":]*user_profile).sum(axis=0)

# SAVE
datatest.loc[:,["userRating", "imdbId","value"]].to_csv("result.csv", sep=',',encoding='utf-8', index=False)