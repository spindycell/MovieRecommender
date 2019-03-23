import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

features = []

data = pd.read_csv("datanot1718.csv")
datatest = pd.read_csv("data1718.csv")
data["userRating"] = pd.to_numeric(data["userRating"])

# Reformat data menjadi Table Fitur

# Mengalikan Bobot Fitur dengan User Rating

# Mendapatkan User Profile

# Scoring

# Save