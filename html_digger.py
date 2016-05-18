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

http_prefix = "http://"


def slurp_page(url):
    try:
        if http_prefix in url:
            r = requests.get(url)
        else:
            r = requests.get(http_prefix + url)
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
    return header_data


# def get_images(url):
#     for link in re.findall('http://sports.cbsimg.net/images/nba/logos/30x30/[A-Z]*.png', source):
#         print link
#
#     try:
#         if http_prefix in url:
#             r = requests.get(url)
#         else:
#             r = requests.get(http_prefix + url)
#         soup = BeautifulSoup(r.text)
#
#         header_data = {}
#
#         for link in soup.findall('http://sports.cbsimg.net/images/nba/logos/30x30/[A-Z]*.png', source):
#             print link
#
#     except Exception as e:
#         logger.error("Cannot open url=%s because of error=%s" % (str(url), str(e)))
