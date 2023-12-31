import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.find('a'))
# print(soup.a)
# print(soup.title)
# print(soup.find(id='score_36296695'))

# print(soup.select('.score'))
# print(soup.select('#score_36296695'))

# links = soup.select('[rel="noreferrer"]')[0]

links = soup.select('[rel="noreferrer"]')
subtext = soup.select('.subtext')
links2 = soup.select('[rel="noreferrer"]')
subtext2 = soup.select('.subtext')

# print(votes[0].get('id'))

mega_links = links + links2
mega_subtext = subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def cerate_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):

		# title = links[idx].getText()
		# href = links[idx].get('href', None)

		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(cerate_custom_hn(mega_links, mega_subtext))