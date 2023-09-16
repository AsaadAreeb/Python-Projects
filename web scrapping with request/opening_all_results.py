import requests, sys, webbrowser, bs4

print('Searching...')
#'https://google.com/search?q='
res = requests.get('https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')


# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')


numOpen = min(5, len(linkElems))

print(numOpen)

for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

