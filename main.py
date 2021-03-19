import csv
import requests
from bs4 import BeautifulSoup
from presentation_scrape import presentation_scrape
from csv_to_excel import convert_to_excel

BASE_URL = "https://ep70.eventpilotadmin.com/web/"
URL = "https://ep70.eventpilotadmin.com/web/page.php?page=Session&project=AAIC19&id=5172&filterUrn=urn%3Aeventpilot%3Aall%3Aagenda%3Afilter%3Acategoryid%3DClinical+%28neuropsychiatry+and+behavioral+neurology%29"


def scrape():

    file = open("output.csv",'w',encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["Abstract #" , "Abstract Title" , "Date" , "Time" , "Location" , "URL" , "Authors" , "Authors Affiliations" , "Abstract Text", "Category" , "Sub Category" , "Session Title"])
    res = requests.get(URL)
    try:
        res.raise_for_status()
    except:
        print("Error in getting Starting page")

    soup = BeautifulSoup(res.text,"html.parser")
    links = soup.findAll(class_ = "catimg")
    presentation_response = requests.get(BASE_URL + links[0]['href'])

    for link in links:
        
        presentation_url = BASE_URL + link['href']
        print("Scraping page : " + presentation_url)
        row = presentation_scrape(presentation_url)
        writer.writerow(row)
    

    print("Scraping Successful !!!")

if __name__=="__main__":
    scrape()
    convert_to_excel()

