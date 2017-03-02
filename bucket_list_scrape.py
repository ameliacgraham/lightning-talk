
from bs4 import BeautifulSoup, SoupStrainer

import requests

for page in range(1,10):
    url = "https://bucketlist.org/category/travel/?page_g={}&querystring_key=page_g".format(page)
    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data)

    for image in soup.find_all(class_='title-info'):
        print image.find("h4").find("a").contents[0]
