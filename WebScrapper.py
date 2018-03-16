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
			#print(html)
			soup=BeautifulSoup(html,'lxml')
			links=soup.select('.a-row .a-link-normal')
			for i in links:
				#print(i['href']) #only want links not the whole section so href is used.
				total_links.append(i['href'])
			print(total_links)


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



      

