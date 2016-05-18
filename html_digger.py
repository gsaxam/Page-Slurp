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
        slurped_data = {}
        for h_count in range(1, 4):
            if soup.find_all('h' + str(h_count)):
                for header in soup.find_all('h' + str(h_count)):
                    try:
                        header_data[header.get_text()] = header.a["href"]
                    except Exception as e:
                        header_data[header.get_text()] = "#"
        # collect all image data
        image_data = get_images(soup)
        # set image_data to 'images' key into header_data
        slurped_data['images'] = image_data
        slurped_data['header_data'] = header_data
        # print(hea)
    except Exception as e:
        logger.error("Cannot open url=%s because of error=%s" % (str(url), str(e)))
    return slurped_data


def get_images(soup):
    img_list = [x['src'] for x in soup.findAll('img')]
    return img_list
