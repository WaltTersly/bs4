from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/tv/features/best-tv-shows-ever-2/")
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")

movie_list = soup.find_all(name="h3", class_ = "jsx-4245974604")
print(movie_list)


# with open("website.html") as file:
#     contents = file.read()


# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text

# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles = soup.select("span.titleline > a")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.get("href")
#     article_links.append(link)

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

# # print(article_texts)
# # print(article_links)

# print(article_texts[largest_index])
# print(article_links[largest_index])