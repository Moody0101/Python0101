import requests as req
from bs4 import BeautifulSoup as bs 
from typing import Union
from itertools import chain
# import countries

list_emails = []
email_beginning = ['social', 'marketing', 'hello', 'contact', 'support', 'info', 'press',
                    'media', 'team', 'sales', 'enquiries', 'help', 'business', 'service',
                    'career', 'community', 'opportunities']

def organizeNames(Names, list_=False):
    if list_ == False:
        return ["".join(i.split()) for i in Names][0]
    else:
        return list(chain.from_iterable([["".join(i.split()) for i in x] for x in Names]))
          
def scrap(url: str = 'https://clutch.co/web-developers') -> str:
    return req.get(url).content

def scrapPages(n=1, pageOne='https://clutch.co/web-developers?page='):
    if n == 1:
        return [i.a.text for i in bs(scrap(), 'html.parser').find_all(class_="company_info")]
    else:
        return [[i.a.text for i in bs(scrap(f"{pageOne}{x}"), 'html.parser').find_all(class_="company_info")] for x in range(n)]
complist = organizeNames(scrapPages(20), list_=True)
print(complist)
