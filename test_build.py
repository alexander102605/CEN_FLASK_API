from dbFunctions import DB
from IPA_Scraper import returnIPA
import requests
connection = DB()


def test_read_false():
    assert len(connection.check_cache("asdvjgavsgd")) == 0

def test_read_true():
    assert len(connection.check_cache("test")) > 0

def test_full_read():
    assert (len(connection.pull_cache())) > 0
    # print(connection.pull_cache())

def test_webscraper_true():
    assert type(returnIPA("en", "word")) is list


# ONLY IF FLASK API IS RUNNING AT localhost:5000, **WILL FAIL OTHERWISE**
def test_flask():
    assert requests.get("http://localhost:5000/?lang=en&word=test").ok

