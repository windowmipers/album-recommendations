import csv

database = {}
data_list = []

with open("albums.csv", "r", newline="") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        album_name = row["Album Name"]
        genres = tuple(row["Genres"].split("/"))
        ranking = int(row["Ranking"].strip())
        year = int(row["Year"].strip())
        data = (ranking, year, genres)
        database[data] = album_name
for d in database:
    data_list.append(d)
genre_results = data_list
year_results = data_list
ranking_results = data_list

def year_search():
    global year_results
    temp_year = []
    while True:
        print("Enter a year or a range of years, e.g. 1980 or 1980-1989:")
        years = input()
        years = years.strip()
        try:
            year = int(years)
            span = False
            break
        except:
            pass
        try:
            spl = years.split("-")
            year1 = int(spl[0])
            year2 = int(spl[1])
            span = True
            break
        except:
            pass
        print("Please enter a valid year or range.")
    if span:
        for item in database:
            if year1 <= item[1] <= year2:
                temp_year.append(item)
    else:
        for item in database:
            if item[1] == year:
                temp_year.append(item)
    if temp_year is not None:
        year_results = temp_year


def ranking_search():
    global ranking_results
    temp_rank = []
    print("Enter a number between 1 and 100 or a range of numbers, e.g. 30 or 11-20:")
    while True:
        rankings = input()
        rankings = rankings.strip()
        try:
            rank = int(rankings)
            span = False
            break
        except:
            pass
        try:
            spl = rankings.split("-")
            rank1 = int(spl[0])
            rank2 = int(spl[1])
            span = True
            break
        except:
            pass
        print("Please enter a valid ranking or range.")
    if span:
        for item in database:
            if rank1 <= item[0] <= rank2:
                temp_rank.append(item)
    else:
        for item in database:
            if item[0] == rank:
                temp_rank.append(item)
    if temp_rank is not None:
        ranking_results = temp_rank


def genre_search():
    global genre_results
    temp_gen = []
    g = []
    while True:
        print("Enter a genre of music:")
        genre = input()
        genre = genre_format(genre)
        g.append(genre)
        while True:
            print("Enter another genre? y/n")
            answer = input()
            answer = answer.lower()
            if answer == "y" or answer == "n":
                break
        if answer == "y":
            continue
        if answer == "n":
            break
    for item in database:
        matches = 0
        for gen in item[2]:
            if genre_format(gen) == genre:
                matches += 1
        if matches == len(g):
            temp_gen.append(item)
    if temp_gen is not None:
        genre_results = temp_gen
    
def genre_format(genre):
    genre = genre.strip()
    genre = genre.lower()
    genre = genre.replace("-", " ")
    return genre



def search():
    remaining_parameters = ["year", "ranking", "genre"]
    first = True
    while remaining_parameters != []:
        parameters_display = "/".join(remaining_parameters)
        if first:
            print(f"What do you want to search by? {parameters_display}")
        else:
            print(f"Do you want to narrow the results by a different parameter? To end search and show results, type end. {parameters_display}/end")
        parameter = input()
        if parameter == "year" and "year" in remaining_parameters:
            year_search()
            remaining_parameters.remove("year")
            first = False
        elif parameter == "ranking" and "ranking" in remaining_parameters:
            ranking_search()
            remaining_parameters.remove("ranking")
            first = False
        elif parameter == "genre" and "genre" in remaining_parameters:
            genre_search()
            remaining_parameters.remove("genre")
            first = False
        elif parameter == "end":
            break
        else:
            print("Please enter a valid parameter.")

def show_results():
    data_list = list(set(year_results) & set(ranking_results) & set(genre_results))
    if not data_list:
        print("No results were found.")
        return
    results_list = []
    for item in data_list:
        results_list.append(database[item])
    results_list.sort()
    print("Here are the results for the criteria you searched:")
    print("********************")
    for album in results_list:
        print(album)
    print("********************")

def main():
    search()
    show_results()

main()
