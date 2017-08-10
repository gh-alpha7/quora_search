from bs4 import BeautifulSoup
import requests
import webbrowser
from selenium import webdriver
inp=input("enter question. ")
string="https://www.google.co.in/search?q=quora"+inp
r=requests.get(string)
soup=BeautifulSoup(r.content,'lxml')
cite=soup.find_all('cite')
ans=cite[0].text
webbrowser.open_new_tab(ans)
    

