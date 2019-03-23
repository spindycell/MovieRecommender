import csv
import numpy as np
import requests

url = "http://www.omdbapi.com/?apikey=e876c8c4&i=tt"

def get(imdb_id):
    return requests.get(url+imdb_id).json()

def getdiract(imdb_id):
    details = get(imdb_id)
    directors = "|".join(str(details["Director"]).split(", "))
    actors = "|".join(str(details["Actors"]).split(", "))
    imdbrat = str(details["Ratings"][0]["Value"]).split("/")
    print([imdb_id, directors, actors, imdbrat])
    if len(imdbrat)!=0:
        imdbrat = float(str(details["Ratings"][0]["Value"]).split("/")[0])
    else:
        imdbrat = 0.0
    return [directors, actors, imdbrat]

def load_csv(file_name):
    result = []
    with open(file_name,"r") as csvfile:
        reader = csv.reader(csvfile)

        for r in reader:
            result.append(r)
    return np.array(result)

def write_csv(file_name, data):
    with open(file_name, "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for d in data:
            writer.writerow(d)

def find_imdb_id(movie_id):
    link = load_csv("links.csv")[1:]
    for data in link:
        if data[0]==movie_id:
            return data[1]

# Load csv files
ratings = load_csv("movie_lens_data/ratings.csv")[1:]
movies = load_csv("movie_lens_data/movies.csv")[1:]
movies1718 = load_csv("movies1718.csv")
idmovies1718 = movies1718[:,0]

# Berdasarkan file explorer.py
selected_user = "111"

datanot1718 = []
for user in ratings:
    if user[0]==selected_user: # user_id = selected_user
        row = []
        for movie in movies:
            if movie[0]==user[1] and movie[0] not in idmovies1718: # movie_id = rated_movie_by_selected_user
                imdb_id = find_imdb_id(user[1])
                row += [user[0], user[2], imdb_id]
                row += [movie[1], movie[2]]
                row += getdiract(imdb_id)
                datanot1718.append(row)
                break

# write_csv("datanot1718.csv", datanot1718)

data1718 = []
for user in ratings:
    if user[0]==selected_user: # user_id = selected_user
        row = []
        for movie in movies:
            if movie[0]==user[1] and movie[0] in idmovies1718: # movie_id = rated_movie_by_selected_user
                imdb_id = find_imdb_id(user[1])
                row += [user[0], user[2], imdb_id]
                row += [movie[1], movie[2]]
                row += getdiract(imdb_id)
                data1718.append(row)
                break

# write_csv("data1718.csv", data1718)


