
import requests
from bs4 import bBeautifulSoup
# URL of the website you want to scrape
url = 'https://example.com'

# Sending a GET request to the URL
response = requests.get(url)

# Checking if the request was successful (status code 200)
if response.status_code == 200:
    # Parsing the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Now you can use BeautifulSoup selectors to extract data
    # For example, let's find all the <a> tags and print their href attributes
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print('Failed to fetch the page. Status code:', response.status_code)
