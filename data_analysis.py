import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import numpy as np
import json
import csv

firefox = webdriver.Firefox(executable_path='/Users/davidgae/miniconda3/bin/geckodriver')
firefox.get('https://tripleseat.com/blog/9-tips-for-marketing-your-craft-brewery')
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
		#need to read more about ligustic parser.
		#collecting words on a page bit more challenging.
		pattern = '1. Get noticed on social media'
		text1 = soup.findAll('h2', text=pattern)
		#print(text1)
		#getvalues.append(text1)

		pattern2 = '2. Partner with local businesses'
		text2 = soup.findAll('h2', text=pattern2)
		#print(text2)
		#getvalues.append(text2)

		pattern3 = '3. Be active in your community '
		text3 = soup.findAll('h2', text=pattern3)
		#print(text3)
		#getvalues.append(text3)

		pattern4 = '4. Focus on what makes you unique'
		text4 = soup.findAll('h2', text=pattern4)
		#print(text4)
		#getvalues.append(text4)

		pattern5 = '5. Launch a newsletter'
		text5= soup.findAll('h2', text=pattern5)
		#print(text5)
		#getvalues.append(text5)
	
		pattern6 = '6. Consider hosting events'
		text6= soup.findAll('h2', text=pattern6)
		#print(text6)
	
		#getvalues.append(text6)
		pattern7 = '7. Highlight what makes your brand fun'
		text7= soup.findAll('h2', text=pattern7)
		#print(text7)
		#getvalues.append(text7)

		pattern8 = '8. Connect with industry publications'
		text8= soup.findAll('h2', text=pattern8)
		#print(text8)
		#getvalues.append(text8)

		pattern9 = '9. Leverage a PR firm'
		text9= soup.findAll('h2', text=pattern9)
		all = [text1,text2,text3,text4,text5,text6,text7,text8,text9]
		#print(text9)
		getvalues.append(all)
	return getvalues

if __name__ == "__main__":
	value = []
	x = 0
	y = 0
	#use tag to collect the script header
	for i, value in enumerate(tags()):
			#https://stackoverflow.com format function with modification
			with open('output.csv', 'w', newline='') as out:
				#for i in value:
				#print(i)
				out.write(str(value,))
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

