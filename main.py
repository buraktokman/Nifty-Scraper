#!/usr/bin/env python3
# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

CONFIG = {	'platform': 'mac', # Change it to 'windows'
			'sleep-page': 5 # seconds
			}


def main():
	global CONFIG

	# START BROWSER
	driver = webdriver.Chrome('./drivers/mac/chromedriver')	# Change 'mac' to 'windows'


	# PAGES
	page = 1
	for i in range(1, 100):

		# GO TO LIST PAGE
		url = f"https://niftygateway.com/marketplace?page={i}&search=&order=&orderType=&onSale=true"
		print(f'page: {i} \t url: {url}')
		driver.get(url)

		# Wait page load
		time.sleep(CONFIG['sleep-page'])


		# GET ALL ITEMS
		#items = driver.find_elements_by_class_name("MuiGrid-root sc-AxmLO gmtmqV MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-4 MuiGrid-grid-md-3 MuiGrid-grid-lg-3")
		items = driver.find_elements_by_css_selector(".MuiCardMedia-root") # Find by price tag


		# GO TO ITEM PAGE
		for item in items:
			# Check if CSS or Item
			# if "$" not in item.get_attribute("innerHTML"):
			# 	continue

			# Click to item
			print(item.get_attribute("innerHTML"))
			item.click()

			# Wait page load
			time.sleep(CONFIG['sleep-page'])


			# SCRAPE ITEM DETAILS
			# Click to 'Market Stats'
			stats_tab = driver.find_elements_by_css_selector(".MuiTab-wrapper")[-1].click()


			# elem = driver.find_element_by_xpath("//*")
			# source_code = elem.get_attribute("innerHTML")

			stats_source = ""

			time.sleep(5) # disable


			exit()


		time.sleep(5) # disable




	# EXIT
	driver.close()




if __name__ == '__main__':
	main()