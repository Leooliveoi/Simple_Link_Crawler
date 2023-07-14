''' Web Crawler :) using BeautifulSoup '''

import sys
import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4

TO_CRAWL = []
CRAWLED = set()
PATTERN = ""

def saveFile():
    print("\nDONE")
    pattern = PATTERN.replace(".","-")
    with open("{}_craw.links".format(pattern), "a") as file:
        list_crawled = set()
        for link in CRAWLED:

            if link not in list_crawled:
                line = "{}\n".format(link)
                file.write(line)

            list_crawled.add(link)


def urlVerify(url):
    if url[:7] == "http://":
        first = url[:7]
        second = url[7:]
    elif url[:8] == "https://":
        first = url[:8]
        second = url[8:]
    elif url[:8] != "https://" or url[:7] != "http://":
        ## Default Protocol to use : HTTPS
        url = "https://"+url

    URL_INIT = url

    return url


def requestVerify(url):

    try:
        urlfinal = urlVerify(url)

        header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
        response = requests.get(urlfinal, headers=header)
        html = response.text
        return html

    except KeyboardInterrupt:
        saveFile()
        sys.exit(0)

    except:
        pass


def getLinks(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tag_a = soup.findAll("a", href=True)
        for tag in tag_a:
            link = tag["href"]
            if link.startswith("http"):
                if PATTERN in link:
                    links.append(link)

        return links
    except:
        pass


def craw():
    while True:
        if TO_CRAWL:
            url = TO_CRAWL.pop()
            html = requestVerify(url)
            links = getLinks(html)

            if links:
                for link in links:
                    if link not in CRAWLED and link not in TO_CRAWL:
                        TO_CRAWL.append(link)

            CRAWLED.add(url)
            print("Crawling {}".format(url))
        else:
            saveFile()
            break


if __name__ == "__main__":
    try:
        if len(sys.argv) >= 3:
            url = sys.argv[1]
            URL_INIT = url

            pattern = sys.argv[2]
            PATTERN = pattern

            TO_CRAWL.append(url)
            craw()
        elif len(sys.argv) == 2:
            print("Need 2 parameters - URL and Pattern")
            print("$python3 {} [URL] [PATTERN]".format(sys.argv[0]))
        else:
            ## A Default Scan DOMAIN
            url = "example.com"
            TO_CRAWL.append(url)
            craw()
    except Exception as e:
        print(e)
