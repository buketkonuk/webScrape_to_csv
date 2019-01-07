from bs4 import BeautifulSoup
import requests
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

rows = []
rows.append(['Source', 'Product Name', 'Price'])
urlList = cfg['url']['urlList']
productClass = cfg['url']['productClass']
prodNameClass = cfg['url']['prodNameClass']
prodPriceClass = cfg['url']['prodPriceClass']


def getSoup(urlList):
	"""This function creates the soup for scraping"""

	response = requests.get(urlList)
	my_soup = BeautifulSoup(response.text, "html.parser")
	#print(my_soup.prettify())
	return my_soup

def getSoupText(urlList):
	"""Soup text is needed later in the output function, a snapshot of the html we scraped"""
	soupText = getSoup(urlList).prettify()	
	return soupText

def webScrape(urlList):
	"""Scrapes the soup and creates the rows object for csv output"""
	
	itemArray= getSoup(urlList).find_all('div', attrs={'class' :productClass})
	itemLen = len(itemArray)
	print(urlList)
	print("number of products on first load= " + str(itemLen))
	# print(itemArray[0].getText())
	for a in range (0,itemLen):
		prodInfo = itemArray[a]
		prodBrand = prodInfo.find('div' , attrs={'class' : prodNameClass})
		prodPrice = prodInfo.find('span', attrs={'class' : prodPriceClass})
		if prodPrice:
			price = prodPrice.getText().lstrip().rstrip()
		else:
			price = "No Price Information"

		rows.append([urlList,
			prodBrand.getText().lstrip().rstrip(),
			price

				])
	return rows


# end of function


for i in urlList:
	webScrape(i)


