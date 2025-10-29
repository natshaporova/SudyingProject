import requests
from bs4 import BeautifulSoup

import re
import json
import sqlite3

newsarticles = list()
newsarticlesLinks = list()
pagesLinks = list()


          
def getNewsLinksFromPage(url,headers,databeseFileName): 
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    outer_divs = soup.find_all('div', class_='result-list-item result-list-item-type-news')
    conn = sqlite3.connect(databeseFileName)
    cursor = conn.cursor()

    for outer_div in outer_divs:
        allarticleLinkstmp = outer_div.find("a", class_="stretched-link")

        if allarticleLinkstmp:
            myhref = allarticleLinkstmp.get('href')
            articleText = getArtclText(urlbase+myhref,headers)

        articleDateTime = outer_div.find("time")
        if articleDateTime:
            datetime_value = articleDateTime.get('datetime')

        cursor.execute(" INSERT INTO articlesMain (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
        conn.commit()
        newArticleid = cursor.lastrowid

        tagsElements = outer_div.find_all("a", class_="tag-item")
        for tgEl in tagsElements:
            curTag=tgEl.text.strip()
            cursor.execute(" INSERT INTO articlesTags (IdArticle,articleTag) VALUES (?,?)", (newArticleid,curTag))
            conn.commit()

    conn.close()        
    
def getArtclText(link, headers):
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')  
    artText = soup.find("div", itemprop="articleBody")
    all_P_pasrt=artText.find_all("p")

    finalTXT=""
    for prt in all_P_pasrt:
        #text_to_print = prt.get_text(strip=True)
        finalTXT +=" "+prt.get_text(strip=True) 
    return finalTXT      

def clean_text(text):
    # Remove leading/trailing whitespace and collapse internal whitespace/newlines
    return re.sub(r'\s+', ' ', text).strip()



def getArticleText(link, headers):
    resultDict = {}
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')  
    body_html_text = soup.find_all("div", class_="news-text-wrap")
    
    resultDict["link"] = link
    resultDict["text"] = ""

    for bd in body_html_text:     
       resultDict["text"] += bd.get_text(strip=True)

    tm = soup.find("time")
    resultDict["date"] = tm.get_text(strip=True) if tm else None
    
    tags = soup.find_all("div", class_="tag-list")
    tag_texts = [a.get_text(strip=False) for a in tags]
    resultDict["tags"] = [clean_text(item) for item in tag_texts]
    
    articles.append(resultDict)


urlbase ="https://www.autobahn.de"
url_firstpage = [
"/aktuelles/news#search",
"/aktuelles/news?tx_kesearch_pi1%5Bpage%5D=2#search"
]
for i in range(3,13):
    url_firstpage.append(f"/aktuelles/news?tx_kesearch_pi1%5Bpage%5D={i}#search") 

# Make a request to the webpage
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS articlesMain (ID INTEGER PRIMARY KEY AUTOINCREMENT,articleDate TEXT, articleText TEXT)")                                                                     
cursor.execute("CREATE TABLE IF NOT EXISTS articlesTags (IdArticle INTEGER,articleTag TEXT)")                                                          
conn.commit()
conn.close()
##################

for i in range(0,10):
   getNewsLinksFromPage(urlbase + url_firstpage[i] ,headers,'newsEvents.db')