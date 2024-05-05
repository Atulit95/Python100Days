from bs4 import BeautifulSoup

with open("WebsiteToScrape.html",encoding="utf8") as file: # Be sure to mention encoding in case if soup not working
        contents=file.read()

soup=BeautifulSoup(contents,"html.parser")
# print(soup.title.string)
# print(soup)

# to find all tags in html doc.
all_anchor_tag=soup.find_all(name="a")
# print(all_anchor_tag)

for tag in all_anchor_tag:
        # print(tag.getText())        getText() is used to get text within tag 
    # print(tag.get("href"))           to find by attribute
    pass
heading=soup.find(name="h1",id="name")   #To find using id, similarly for class
# print(heading.string)

company_url=soup.select_one(selector="p a")
# print(company_url)

name=soup.select_one(selector="#name")      # To select via id
# print(name)

headings=soup.select(selector=".heading")
print(headings)