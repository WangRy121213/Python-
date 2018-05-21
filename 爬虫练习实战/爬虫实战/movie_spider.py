# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
import re
import requests
import json
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def getMovieLinks():
    r  = requests.get('http://www.movie-list.com/archive.php')
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    baseurl ='http://www.movie-list.com'
    links =[]
    for link in soup.find_all('a',href=re.compile('/trailers/.+')):
        newurl = baseurl+link.get('href')
        if newurl not in links:
            links.append(baseurl+link.get('href'))
    return links
        
def crawlMovieItem(url):
    mr  = requests.get(url)
    mdata = mr.text
    msoup = BeautifulSoup(mdata,"lxml")
    div =msoup.find('div',style='padding-left:168px;')
    name = div.h1.text.lstrip()
    releasedate = div.find('span',style='color:#181818; font-size:12px;').text.lstrip()
    director = div.find('span',itemprop='director').find('span',itemprop='name').text.lstrip()
    actors = [x.text.lstrip() for x in div.find('span',class_='cast').find_all('span',itemprop='name')]
    genre = [x.lstrip() for x in div.find('span',itemprop='genre').text.split(',')]
    linkpattern = re.compile('imdb.com/title/.*')
    link = msoup.find('a',href=linkpattern).get('href')
    pattern = re.compile('imdb.com/title/(tt\d*)/')
    id = re.search(pattern,link).group(1)
    link = 'http://www.imdb.com/title/'+ id
    print(id)
    #link = 'http:'+div.find('span',class_='links-meta').a.get('href')
    ratingcount = msoup.find('span',itemprop='ratingCount').text.lstrip()
    ratingvalue = msoup.find('span',itemprop='ratingValue').text.lstrip()
    imglink = 'http://www.movie-list.com' + msoup.find('img',itemprop='image').get('src')
    movie={'name':name,'releasedate':releasedate,'director':director,'actors':actors,'genre':genre,'link':link,'imglink':imglink,'ratingcount':ratingcount,'ratingvalue':ratingvalue}
    return movie

def saveToEs(movie,i):
    print('try to save '+ str(movie))
    es.index(index='movie', doc_type='movie', id=i, body=movie)
    
def crawlAndSave():
    try:
        links = getMovieLinks()
        id =0
        for link in links:
            try:
                print('try to download '+link)
                movie = crawlMovieItem(link)
                saveToEs(movie,id)
                id +=1
            except AttributeError:
                print('AttributeError')
            except ConnectionError:
                print('ConnectionError')
    except ConnectionError:
                print('ConnectionError')

crawlAndSave()
