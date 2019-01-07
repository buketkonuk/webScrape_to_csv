import csv
import yaml
from datetime import datetime
import time
import sys
from scraper import rows, getSoupText

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

urlList = cfg['url']['urlList']


def output(rows, urlList):

	dt = datetime.now()
	dt = dt.replace(minute=0, second=0, microsecond=0)
	dtstring = str(dt) 
				#print(dtstring)
	newformatdt=(dtstring.replace(":","_")).replace(" ", "_")
				#print(newformatdt)
	scriptName = sys.argv[0].split("\\")[-1][0:-3]
		#the script without the .py extension    
				#print(scriptName)


	with open( "DM-" + str(scriptName) + "_" + newformatdt + '.csv','w', newline='') as f_output:
	 		csv_output = csv.writer(f_output)
	 		csv_output.writerows(rows)

	for i in range(0,len(urlList)):
		with open("DM-" + str(scriptName) + "_" + newformatdt + '.html', 'a') as txt_file:  
				txt_file.write("Date and time of Scraping Data = " + str(datetime.now())+ '\n')
				txt_file.write( "Page scraped = " + urlList[i] + '\n')
				txt_file.write( "=========DRINKS CONTENT STARTS HERE============"+'\n')
				txt_file.write(getSoupText(urlList[i]))

output(rows, urlList)
# END OF WRITE FUNCTION