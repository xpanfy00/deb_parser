from deb_parse.parser import Parser
import argparse
import requests
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--package", default="~/downloads/curl_7.19.7-1ubuntu1.11.deb")
parser.add_argument("-l", "--changelog",required=False, action='store_true', help="changelog")
args = parser.parse_args()
name = args.package
list = name.split("/")
name = list[2]
urlList = name.split(".deb")
list = name.split("_")
name = list[0]
urlName = name[0]
URL = 'https://changelogs.ubuntu.com/changelogs/pool/main/' + urlName + "/" + name + "/" + urlList[0] + "/" + "changelog"
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/90.0.4430.212 Safari/537.36', 'accept': '*/*'}

path = "/var/lib/dpkg/status"
my_parser = Parser(path)
list = my_parser.raw_pkg_info
def main(name):
    print(name)
    i = 0
    while i < len(list):
        item = list.__getitem__(i)
        if item.get("name") == name:
            details = item.get("details")
            print("Package name: " + item.get("name"))
            print("Package version: " + details.get("version"))
            print("Package dependencies: " + details.get("depends"))
            print("")
        i = i + 1

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.find()
    print(text)



def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)


if __name__ == "__main__":
    main(name)
    if args.changelog:
        parse()
    else:
        parse()
        print("Done!")

