from bs4 import BeautifulSoup as soup
import requests

START_YEAR = 2013
END_YEAR = 2015
BASE_TARGET_URL = "http://www.who.int/csr/don/archive/year/"

def parse_string(el):
	text = ''.join(el.find_all(text=True))
	return text.strip()

for year in range(START_YEAR,END_YEAR):
	page = requests.get(BASE_TARGET_URL + str(year) + "/en/")
	tree = soup(page.text)
	
	archiveLinks = tree.find_all("span", {"class": "link_info"})
	
	for linkInfo in archiveLinks:
		print linkInfo.text.strip()
		
		itrLink = linkInfo
		while itrLink.previous_sibling != None:
			itrLink = itrLink.previous_sibling;
			if itrLink.name == "a":
				print itrLink.attrs['href']
				print ""
				break
	
	print "------------------------------- END " + str(year) + "-------------------------------"
	print ""