import requests
from bs4 import BeautifulSoup
from abstract_scrape import get_abstract

BASE_URL = "https://ep70.eventpilotadmin.com/web/"
URL = "https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=28489"


def presentation_scrape(url):
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        print("Error in getting page" + url)

    soup = BeautifulSoup(res.text,"html.parser")
    abstract_number = soup.find(class_ = "sessionnumber").get_text()

    abstract_wrapper = soup.find(class_="session_detail_title_708")
    abstract_span = abstract_wrapper.find("span")
    abstract_title = abstract_span.get_text()

    date_time = soup.findAll(class_ ="session_detail_day")

    time = date_time[0].get_text().strip()
    date = date_time[1].get_text().strip()


    location_wrapper = soup.find(class_="session_detail_location")
    location = location_wrapper.find("span").get_text().strip()

    cat = soup.findAll(class_ = "filter_value")
    category = cat[0].get_text().strip()
    sub_category = cat[1].get_text().strip()


    author_block = soup.find('b',string="Author Block:")
    author_details = list(author_block.next_siblings)

    authors = author_details[1].get_text().strip()
    try:
        authors_affiliation = author_details[2].split(',')[1].strip()
    except:
        authors_affiliation = ""


    abstract_wrapper= soup.find(class_="list_cell_title").parent.parent
    abstract_path = abstract_wrapper['href']
    abstract_url = BASE_URL+abstract_path
    abstract_text = get_abstract(abstract_url)

    session_wrapper = soup.find(class_ = "session_title")
    session_title = session_wrapper.find("span").get_text().strip()

    data = [abstract_number,abstract_title,date,time,location,url,authors,authors_affiliation,abstract_text,category,sub_category,session_title]
    return data



