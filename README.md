# csupdate

This repository and Python script watches for changes on a CityStrides city of one's choosing.

Setup
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install --upgrade pip
```

Configure
```
vi config.py
# add your Pushbullet key, if notifications are desired
# add the url for your CityStrides city
# we shouldn't have to change the target_class unless the website changes
```

Test at the Terminal
```
# make sure you activate venv first
python scrape.py
python scrape.py
```

Add repeating script run to Crontab
```
crontab -e

*/10 * * * * cd /getlab/dpb6/repos/csupdate && /getlab/dpb6/repos/csupdate/venv/bin/python /getlab/dpb6/repos/csupdate/scrape.py
```

