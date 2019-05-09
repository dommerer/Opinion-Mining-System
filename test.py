import requests
import re

url = "https://th.tripadvisor.com/Attraction_Review-g293917-d7133132-Reviews-Maya_Lifestyle_Shopping_Center-Chiang_Mai.html"
data = requests.get(url);
from bs4 import BeautifulSoup;

soup = BeautifulSoup(data.text,'html.parser');

name    = soup.find_all("div",{"class":"info_text"});                   
date    = soup.select('div.ui_column > span.ratingDate'); 
rating  = soup.select('div.ui_column > span.ui_bubble_rating');  
title   = soup.find_all("span",{"class":"noQuotes"});   
comment = soup.find_all("div",{"class":"prw_rup prw_reviews_text_summary_hsx"});         #ความคิดเห็น

for a,b,c,d,e in zip(name,date,rating,title,comment):
    a1 = a.text
    b1 = b.get('title')
    c1 = c.get('class')[1].split('bubble_')[1].split('0')[0]
    d1 = d.text
    e1 = e.text

    print("Name:",a1);
    print("Date:",b1);
    print("Rating:",c1);
    print("Title:",d1);
    print("Descript:",e1);
        

    print("*************************************\n");
    
x = len(rating);

print("count:",x,"\n")
