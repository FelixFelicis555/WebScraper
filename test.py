import requests
from bs4 import BeautifulSoup
result=[]
all_features=[]

#Accessing the Web Page which is going to be Scrapped.
#page=input("Enter the web page you want to scrap :")
#r=requests.get("https://www.daraz.pk/mi-redmi-4x-5.0-3gb-ram-32gb-rom-fingerprint-sensor-golden-6728248.html")
r=requests.get("https://www.flipkart.com/redmi-note-4-black-64-gb/p/itmeqe48766xqzb7?pid=MOBEQ98TABTWXGTD&srno=b_1_1&otracker=offerslist&lid=LSTMOBEQ98TABTWXGTDNZ53XZ&fm=neo/merchandising&iid=79d26909-951e-4478-838b-6b739cc7e9b5.MOBEQ98TABTWXGTD.SEARCH&ppt=Store%20Browse&ppn=Search%20Page&ssid=wt803pigbli9yrcw1521140713062")
if r.status_code == 200: #Checking the status of page whether it exists or not
	html=r.text #fetching the text of the webpage and printing it
	#print(html)
	soup=BeautifulSoup(html,'lxml') #lxml is our parser

	#Title Innformation
	title_section=soup.find('h1')
	#print(Title)
	if title_section:
		title=title_section.text
		print(title)

	#Price Information
	price_section=soup.select('._1vC4OE')
	price=price_section[0].text.replace(',','')
	print(price)

	#Features Information
	feature_section=soup.select('._2-riNZ')
	#print(feature_section)
	for feature in feature_section:
		print(feature.text)
		all_features.append(feature.text)
	all_features='|'.join(all_features)


	result.append(title)
	result.append(price)
	result.append(all_features)
	output=','.join(result)

	with open('output.txt','a+',encoding='utf') as file:
		file.write("Title,Price,Features\n")
		file.write(output)



