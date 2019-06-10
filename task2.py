import requests
from bs4 import BeautifulSoup

urls = ["http://github.com/", "https://github.com/", "https://www.github.com/", "https://www.github.com/test/", "https://github.com/testlololo", "https://github.com/test?lol"]

def get_result_data(resp):
	soup = BeautifulSoup(resp.text, "html.parser")
	page_title = soup.title.text
	h1_text = soup.h1.text
	meta_desc = soup.find('meta', {'name' : 'description'})
	return "page_title: \"{}\"\nh1_text: \"{}\"\nmeta_desc: \"{}\"".format(page_title, h1_text, meta_desc)


for url in urls:
	resp = requests.get(url, allow_redirects=False)
	print("{}. {}".format(str(urls.index(url)+1), url))
	print("code: {}".format(str(resp.status_code)))
	if resp.status_code == 200:
		print(get_result_data(resp))


