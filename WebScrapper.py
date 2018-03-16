import requests
from bs4 import BeautifulSoup
result=[]
all_features=[]

#Accessing the Web Page which is going to be Scrapped.
page=input("Enter the web page you want to scrap :")
r=requests.get(page)
if r.status_code == 200: #Checking the status of page whether it exists or not
	html=r.text #fetching the text of the webpage and printing it
	soup=BeautifulSoup(html,'lxml') #lxml parser is being used for parsing.

	#Title Innformation
	title_section=soup.find('h1')
	if title_section:
		title=title_section.text
		print(title)

	#Price Information
	price_section=soup.select('._1vC4OE')
	if price_section:
		price=price_section[0].text.replace(',','')
		print(price)

	#Features Information
	feature_section=soup.select('._2-riNZ')
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



