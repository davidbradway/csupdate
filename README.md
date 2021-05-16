

```
python -m venv venv
pip install -r requirements.txt
pip install --upgrade pip

crontab -e

*/10 * * * * /getlab/dpb6/repos/csupdate/venv/bin/python /getlab/dpb6/repos/csupdate/scrape.py
```

