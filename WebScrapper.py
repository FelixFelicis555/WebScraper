import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}


def parse(u):
	return 'Parsed...{0}'.format(u)

def fetch(category_url):

	
