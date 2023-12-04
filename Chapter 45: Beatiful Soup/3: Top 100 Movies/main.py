import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movie_webpage = response.text
# print(movie_webpage)

soup = BeautifulSoup(movie_webpage, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movies_title = [movies.getText() for movies in all_movies]
movies = movies_title[::-1]

with open('best_movies.txt', "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")