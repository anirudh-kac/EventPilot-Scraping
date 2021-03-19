#Author : Anirudh Kachroo
#gets abstract text from the abstract page

import requests
from bs4 import BeautifulSoup


def get_abstract(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        print("Error in getting page" + url)
    soup = BeautifulSoup(res.text,"html.parser")

    all_text = soup.find(class_="abstract").getText().strip()
    split = all_text.split("\n")

    abstract = "\n".join(split[5:])
    return abstract

#print(get_abstract("https://ep70.eventpilotadmin.com/web/page.php?page=IntHtml&project=AAIC19&id=28496"))


