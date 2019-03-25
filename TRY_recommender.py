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
                    data.loc[index, f] = 1.0 * data.loc[index, "userRating"]
            elif i < 23:
                if f in row["directors"]:
                    data.loc[index, f] = 0.2 * data.loc[index, "userRating"]
            elif i < 35:
                if f in row["actors"]:
                    data.loc[index, f] = 0.3 * data.loc[index, "userRating"]
    data = data.drop(["title","userId","imdbRating","genres","directors","actors"],axis=1)
    return data

data = reformat(data, features)
data.to_csv("data_terformat.csv", index=False)

# Mendapatkan User Profile
user_profile = data.loc[:,"Comedy":].sum(axis=0) #axis 0 = jumlah ke bawah
#user_profile = user_profile / user_profile.sum()
print(user_profile) 

# Scoring
datatest = reformat(datatest, features)
datatest.to_csv("datatest_terformat.csv", index=False)

datatest["Score"] = 0.0
for index, row in datatest.iterrows():
    datatest.loc[index, "Score"] = (datatest.loc[index, "Comedy":] * user_profile).sum(axis=0)
print(datatest["Score"])

# Save
datatest.loc[:,["userRating","imdbId","Score"]].to_csv("result.csv")