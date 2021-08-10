#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests


# This project is made only for educational purpose with no harm intentions
# I do not own any of the content from hacker news

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)


# using list comprehension to only get the score point of the article in integer format
article_upvotes = [int(score.getText().split()[0])
                   for score in soup.find_all(name="span", class_="score")]

largest_num = max(article_upvotes)
largest_index = article_upvotes.index(largest_num)

print(f"The most voted article on the hacker news right now with {largest_num} upvotes is:\n\
    The article heading --> {article_texts[largest_index]}\t\t |\t \n\
    See full article here --> {article_links[largest_index]}\n ")
    
