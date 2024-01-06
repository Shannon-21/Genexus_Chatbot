# processing
import pandas as pd
import os

# scrapping
from bs4 import BeautifulSoup
import requests


class Scrapping():
    def __init__(self, url:str):
        self.url = url
        self.df_menu = pd.DataFrame()
    
    def get_response(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def scrape_menu(self):
        soup = self.get_response()
        menu = soup.find_all('li')[3].find_all('a')
        
        refs = []
        titles = []
        
        for ref in menu:
            refs.append(f"https://wiki.genexus.com/{ref.get('href')}")
            titles.append(ref.text)
        
        self.df_menu['Title'] = titles
        self.df_menu['Link'] = refs
    
    def scrape_page(self, url_page):
        '''Extrae el texto del divisor con la clase que abarca el contenido de la página'''
        # consulta al link de la página
        print('i find a page...')
        response = requests.get(url_page)
        soup = BeautifulSoup(response.text, 'html.parser')

        # encuentra el divisor deseado
        wiki_body = soup.find_all("div", class_="TableWikiBody")[0]

        # extrae todo el texto del divisor
        extracted_text = []
        for element in wiki_body.find_all(recursive=False):
            extracted_text.append(element.text.strip())

        # concatena a un unico string
        texto_final = '\n'.join(extracted_text)
        print('i scrapped it.\n')
        return texto_final
    
    def scrape_pages(self):
        self.df_menu['Content'] = self.df_menu['Link'].apply(self.scrape_page)
    
    def scrape_wiki(self):
        self.scrape_menu()
        self.scrape_pages()
        self.df_menu.to_csv('genexus_wiki.csv')


if __name__=="__main__":
    if not os.path.isfile('genexus_wiki.csv'):
        url = "https://wiki.genexus.com/commwiki/wiki?6426,Inline+Formulas+within+a+contextual+table"
        scrapping = Scrapping(url)
        scrapping.scrape_wiki()


