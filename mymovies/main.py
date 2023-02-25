from bs4 import BeautifulSoup
import requests

page_root = 'https://www.mymovies.it/film/2022/?orderby=mymonetro&p='
movies = []
N_PAGES = 5

for page in range(1, N_PAGES):
    response = requests.get(page_root + str(1))
    soup = BeautifulSoup(response.text, 'html.parser')

    titles = soup.find_all(name='div', class_='schedine-titolo')
    data = soup.find_all(name='div', class_='schedine-lancio')
    n_films = len(titles)

    if n_films != len(data):
        print('ERROR: we are missing something!')

    counter = 0
    for title in titles:
        try:
            durata = int(str(data[counter].select('div strong')).split()[1])
        except:
            durata = 999
        movie = {'title': title.getText(), 'link': title.a['href'],
                    'durata': durata, 'ranking': counter + 1}
        movies.append(movie)
        counter = counter + 1

# for index in range(0, n_films-1):
#     print(index)
#     title = titles[index]
#     movie = {'title': title.getText(), 'link': title.a['href'],
#             'durata': int(str(data[index].select('div strong')).split()[1]),
#             'ranking': index + 1}
#     print(movie)
#     movies.append(movie)

print(movies)
movies_sorted = sorted(movies, key=lambda x: x['durata'], reverse=True)
print(movies_sorted)


# # ---------------------------- Beautiful soup exercise
# response = requests.get('https://news.ycombinator.com/news')
# web_page = response.text
#
# soup = BeautifulSoup(web_page, 'html.parser')
# article_tags = soup.find_all(name='span', class_ = 'titleline')
# votes = [int(vote.getText().split()[0]) for vote in soup.find_all(name='span', class_='score')]
#
# articles = []
# counter = 0
#
# for tag in article_tags[0:-1]:
#     text = tag.getText()
#     article = {'title': text}
#     link = tag.a['href']
#     article['link'] = link
#     article['upvote'] = votes[counter]
#     articles.append(article)
#     counter = counter + 1
#
# print(articles[2])
# print(articles[2]['upvote'])
#
# articles_sorted = sorted(articles, key=lambda x:x['upvote'], reverse=True)
## -------------------------  Beautiful soup helps
# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# soup.tag to read HTML
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find_all(name='a'))
# -------------------------------
# all_anchor_tags = soup.find_all(name='a')
# for tag in all_anchor_tags:
#     print(tag.get('href'))
#
# print(soup.find('h1', id='name'))
# print(soup.find_all("h3", class_="heading"))
# print(soup.select("body a"))
# print(soup.select_one("#name"))
# print(soup.select_one('.heading'))
