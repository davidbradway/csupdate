import os
import pickle
import requests
from bs4 import BeautifulSoup
from pushbullet import Pushbullet
import config


def main():
    cache_file = 'last_date.pkl'
    if os.path.exists(cache_file):
        with open(cache_file, 'rb') as cache_handle:
            print("using cached result from '%s'" % cache_file)
            old_string = pickle.load(cache_handle)
    else:
        old_string = ''

    url = 'https://citystrides.com/cities/171335'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mt-1")
    date_string = results.get_text()

    if date_string != old_string:
        print('New Streets!', date_string)

        pb = Pushbullet(config.api_key)
        pb.push_note("New Streets!", date_string)

        with open(cache_file, 'wb') as cache_handle:
            print("saving result to cache '%s'" % cache_file)
            pickle.dump(date_string, cache_handle)
    else:
        print('same')


if __name__ == "__main__":
    main()
