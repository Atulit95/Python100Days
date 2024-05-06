from bs4 import BeautifulSoup
import requests

response=requests.get("https://news.ycombinator.com")

yc_webpage=response.text

soup=BeautifulSoup(yc_webpage,"html.parser")
# all_anchor_tag=soup.find_all("a")
# print(all_anchor_tag)

# for tag in all_anchor_tag
articles=soup.find_all(name="span",class_="titleline")
# print(articles)
article_texts=[]
article_links=[]
for article_tag in articles:
    text=article_tag.getText()
    article_texts.append(text)
    links=article_tag.find("a").get("href")
    article_links.append(links)

print(article_links)
print(article_texts)


articles_links=[title.get("href") for title in articles]
# print(articles_links)
# article_link=articles.get("href")
# print(article_link)

articles_score=[score.getText() for score in soup.find_all(name="span",class_="score")]
print(articles_score)