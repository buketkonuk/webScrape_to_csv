# Web Scrape via BeautifulSoup and write the data into a  csv file
Script for scraping data from Website and writing the data into csv file
The objectives:

1- Grab the product information (Brand name, Product name, price and any additional info) from a commercial website 

2- Clean the data in the format we want

3- Write into a csv file for database integration

There are three scripts to achieve these objectives. The user can first test whether the website allows scraping via the testUrl with the file 'testScraper.py'. On this script, the product information class on the html source is used for testing. The output is the number of products on the webpage.

The main Scraper is 'scraper.py'. This script reads the necessary html classes from the config file creates the 'rows' for csv output.

Finally the 'out-tocsv.py' reads the rows, grabs the soup as text for html output and writes it all out with the datetime of today as filename.
