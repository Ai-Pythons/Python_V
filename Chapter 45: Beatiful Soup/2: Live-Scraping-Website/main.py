from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article = soup.find_all(name="span", class_="titleline")
# print(article_tag)
# links = article_tag.find('a')['href']
# print(links)

article_texts = []
article_links = []

for article in article:
    article_text = article.get_text()
    article_texts.append(article_text)
    
    article_link = article.find('a')['href']
    article_links.append(article_link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

lowest_number = min(article_upvotes)
lowest_index = article_upvotes.index(lowest_number)

print(article_texts[largest_index])
print(article_links[largest_index])

print(article_texts[lowest_index])
print(article_links[lowest_index])
