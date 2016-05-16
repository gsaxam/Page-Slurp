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
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.text)

        header_data = {}
        for h_count in range(1, 4):
            if soup.find_all('h' + str(h_count)):
                for header in soup.find_all('h' + str(h_count)):
                    try:
                        header_data[header.get_text()] = header.a["href"]
                    except Exception as e:
                        header_data[header.get_text()] = "#"

    except Exception as e:
        logger.error("Cannot open url=%s because of error=%s" % (str(url), str(e)))
    print header_data
    return header_data
