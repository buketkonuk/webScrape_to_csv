from bs4 import BeautifulSoup
import requests

import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

productClass = cfg['url']['productClass']
urlTest = cfg['url']['urlTest']

def ScrapeTest():

	response = requests.get(urlTest)
	my_soup = BeautifulSoup(response.text, "html.parser")
	#print(my_soup.prettify())

	soupText = my_soup.prettify()
	
	itemArray= my_soup.find_all('div', attrs={'class' :productClass})
	itemLen = len(itemArray)
	print(urlTest)
	print("number of products on first load= " + str(itemLen))
	# print(itemArray[0].getText())

# end of function

ScrapeTest()