import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}


def parse(u):
	return 'Parsed...{0}'.format(u)

#fetch method will fetch the total links and total pages in the url/webpage

def fetch(category_url):
	total_pages=0
	total_links=[]
	try:
		r=requests.get(category_url,headers=headers,timeout=5)
		if r.status_code==200:
			html=r.text
			soup=BeautifulSoup(html,'lxml')
			#Getting all the links from one page.
			links=soup.select('.a-row .a-link-normal')
			for i in links:
				total_links.append(i['href'])
			#Getting the total pages.
			total_pages=155
		for x in range(2, total_pages + 1):
			#sleep(2)
			cat_url = 'https://www.amazon.in/s/ref=sr_pg_{0}?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A!976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_n_operating_system_browse-bin%3A1485077031&page=4&bbn=1389432031&ie=UTF8&qid=1521200739'.format(x)
			#print('Processing...' + cat_url)
			r = requests.get(cat_url, headers=headers, timeout=5)
			if r.status_code == 200:
				html = r.text
				soup = BeautifulSoup(html, 'lxml')
				links = soup.select('.a-row .a-link-normal')
				for i in links:
					total_links.append(i['href'])
		print(len(total_links))


	except requests.ConnectionError as e:
		print("OOPS!! Conection Error. Make sure you are connected to Internet. Technical Details are : \n")
		print(str(e)) #Error Thrown
	except requests.Timeout as e:
		print("OOPS!! Timeout Issue")
		print(str(e))
	except requests.RequestException as e:
		print("OOPS!! General Error")
		print(str(e))
	except requests.KeyboardInterrupt:
		print("Someone Closed the Program")

	finally:
		pass

def main():
	category_url="https://www.amazon.in/s/ref=lp_1389432031_nr_p_n_operating_system_0?fst=as%3Aoff&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cn%3A1389432031%2Cp_n_operating_system_browse-bin%3A1485077031&bbn=1389432031&ie=UTF8&qid=1521195719&rnid=1485076031"
	fetch(category_url)


if __name__ == '__main__':
	main()



      

