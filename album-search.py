import csv

database = {}
with open("albums.csv", "r", newline=" ") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        album_name = row["Album Name"]
        genres = row["Genres"].split(", ")
        ranking = row["Ranking"]
        year = row["Year"]
        data = [ranking].extend([year].extend(genres))
        database[data] = album_name

def main():
    print("What do you want to search by? year/ranking/genre"
    parameter = input()
    
