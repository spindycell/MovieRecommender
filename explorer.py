import csv
import numpy as np

def load_csv(file_name):
    result = []
    with open(file_name,"r") as csvfile:
        reader = csv.reader(csvfile)

        for r in reader:
            result.append(r)
    return np.array(result)

# Load csv files
ratings = load_csv("movie_lens_data/ratings.csv")[1:]
movies1718 = load_csv("movies1718.csv")
idmovies1718 = movies1718[:,0]

# Mencari user yang cocok untuk dijadikan contoh
totrat = [0]*611 # total rating tiap user untuk semua film
m17rat = [0]*611 # total rating tiap user untuk film 2017-2018
updateduser = [] # daftar user yang pernah merating film 2017-2018
for user in ratings:
    totrat[int(user[0])] += 1
    if user[1] in idmovies1718:
        updateduser.append(user[0])
        m17rat[int(user[0])] += 1
updateduser = set(updateduser)

# print(sorted(m17rat))
print("Banyak user update :", len(updateduser))
print()
print("1st")
print("Rating film(2017-2018) paling banyak:", sorted(m17rat)[-1], "rating oleh user", m17rat.index(sorted(m17rat)[-1]))
print("Total rating user", m17rat.index(sorted(m17rat)[-1]), ":", totrat[m17rat.index(sorted(m17rat)[-1])])
print()
print("2nd")
print("Rating film(2017-2018) paling banyak:", sorted(m17rat)[-2], "rating oleh user", m17rat.index(sorted(m17rat)[-2]))
print("Total rating user", m17rat.index(sorted(m17rat)[-2]), ":", totrat[m17rat.index(sorted(m17rat)[-2])])

