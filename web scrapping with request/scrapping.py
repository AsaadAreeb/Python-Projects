import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()

    playFile = open('RomeoAndJuliet.txt', 'wb')

    for chunk in res.iter_content(100000):
        playFile.write(chunk)
except Exception as exc:
    print('There was a problem: %s' % (exc))