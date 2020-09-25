from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# path="./geckodriver"
# driver=webdriver.Firefox(path)

driver = Firefox()
#Or use the context manager
from selenium.webdriver import Firefox

   #your code inside this indent




#setup proxy
file=open("proxy.txt", "r")
proxies = file.readlines()
for proxy in proxies :

	proxy="<"+proxy.strip()+">"
	print(proxy)

	# PROXY = "<HOST:PORT>"
	webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
	    "httpProxy": proxy,
	    "ftpProxy": proxy,
	    "sslProxy": proxy,
	    "proxyType": "MANUAL",

	}

	driver.get("https://www.youtube.com/")
	WebDriverWait(driver, 10)
	driver.quit()


		# search=driver.find_element_by_name("search_query")
		# search.send_keys("4k")
		# search.send_keys(Keys.RETURN)
		#
		# try:
		# 	#print(driver.page_source)
		# 	main = WebDriverWait(driver, 10).until(
		# 	    EC.presence_of_element_located((By.ID, "content")))
		# 	videos=main.find_elements_by_class_name("style-scope ytd-search-pyv-renderer")
		# 	for video in videos :
		# 		header= video.find_element_by_id("video-title")
		# 		print(header.text)
		# finally:
