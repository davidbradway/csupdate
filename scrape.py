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

    page = requests.get(config.url, timeout=5)
    soup = BeautifulSoup(page.content, 'html.parser')
    page.close()
    results = soup.find(class_=config.target_class)
    date_string = results.get_text()
    ul = soup.find('ul')  # Start here
    lis = []
    for li in ul.findAll('li'):
        lis.append(li)
    result2 = lis[1].find('a')
    streets = result2.get_text()

    print(streets + date_string)
    if date_string != old_string:
        if config.api_key != 'replaceme':
            pb = Pushbullet(config.api_key)
            pb.push_note(streets, date_string)

        with open(cache_file, 'wb') as cache_handle:
            print("saving result to cache '%s'" % cache_file)
            pickle.dump(date_string, cache_handle)
    else:
        print('same')


if __name__ == "__main__":
    main()
