# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:37:35 2018

@author: Awal
"""
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
#import numpy
page = requests.get("https://www.rottentomatoes.com/m/black_panther_2018/reviews/")

#soup=BeautifulSoup(page.content,'html.parser')
#review=soup.find_all('div',class_='the_review')
cleantext = BeautifulSoup(page.content, "lxml")
review=cleantext.find_all('div',class_='the_review')
#print(review[0].prettify)
paragraphs = []
for x in review:
    paragraphs.append(str(x))

countn=countp=counto=0    
for i in paragraphs:
    blb=TextBlob(i).sentiment.polarity
    print(TextBlob(i).sentiment.polarity)
    if(blb<0):
        print("Negative")
        countn+=1
    elif(blb>0):
        print("Positive")
        countp+=1
    else:
        print("Neutral")
        counto+=1
total=countn+countp+counto
perp=(countp*100)/total
pern=(countn*100)/total  
print("Critics that liked the movie :"+str(perp) + "%" )
print("Critics that didn't liked the movie :"+ str(pern)+"%")
    