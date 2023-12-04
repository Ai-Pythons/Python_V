from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
# print(soup.h3)
# print(soup.title)

all_anchor_tags = soup.find_all(name="a")

# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
    
heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
# print(company_url)

name_id = soup.select(selector="#name")
print(name_id)

headings = soup.select(selector=".heading")
print(headings)