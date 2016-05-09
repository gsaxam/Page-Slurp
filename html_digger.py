"""
author: saksham.ghimire
email: gsaxam@gmail.com
date: 05/08/2016
"""
import requests
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def slurp_page(url):
    h2_list = list()
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        h2_list = [header.get_text() for header in soup.find_all('h2')]

    except Exception as e:
        logger.error("Cannot open url=%s because of error=%s" % (str(url), str(e)))

    return h2_list
