from urllib.parse import urlparse
from html.parser import HTMLParser
import os
import re
import requests
from bs4 import BeautifulSoup

                
                                       

class Scraper():
    def __init__(self,url):
         text=requests.get(url).text
         self.text=text
         
         
        
        
        
    