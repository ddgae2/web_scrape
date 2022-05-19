import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import json
import csv

firefox = webdriver.Firefox(executable_path='/Users/davidgae/miniconda3/bin/geckodriver')
firefox.get('https://www.yahoo.com')
content = firefox.page_source
soup = BeautifulSoup(content, 'html.parser')

def check():
    check = { int: np.results, float: np.float, str: np.rlist }
    return check

#tags
def tags():
	tags = []
	getvalues = []
	for tag in soup.findAll(True):
		getvalues.append(tag)
	return getvalues

if __name__ == "__main__":
	value = []
	x = 0
	y = 0
	#use tag to collect the script header
	for i, value in enumerate(tags()):
		if value.name == 'script':
			#store as a pandas
			df5= pd.DataFrame(value)
			result = df5.to_json(orient="split")
			parsed = json.loads(result)
			#convert to json
			new = json.dumps(parsed, indent=4)
			print(new)
			img = len(soup.findAll('img'))
			print("Images: ",img)
			#https://stackoverflow.com format function with modification
			with open('output.csv', 'w', newline='') as out:
				for i in range(0,img):
					out.write('{0},'.format(i))
					out.write('\n')


	# Checking for web address changes, need to confirm.
	https = []
	a = []
	b = []
	line1 = []
	for i,https in enumerate(soup.findAll('a')):
		# print(https.get('href'))
		name = https.find('href')
		line1.append(name)
		num = len(line1)
	# https://stackoverflow.com format function with modification
	with open('output2.csv', 'w', newline='') as out:
		for i in range(0, num):
			out.write('{0},'.format(i))
			out.write('\n')

