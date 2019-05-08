import requests
import re
from bs4 import BeautifulSoup
import pickle


content = None

# get urls from file
with open('output.txt', 'r') as f:
    content = f.read()

regex = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

websites = re.findall(regex, content)

requests.packages.urllib3.disable_warnings()
for website in websites:
    try:
        # website = website.replace('http', 'https', 1)
        print("trying " + website)
        resp = requests.get(website, verify=False)
        html_doc = resp.text
        soup = BeautifulSoup(html_doc, 'html.parser')
        links = soup.findall('a')
        print(links)
        quit()
    except:
        print("something wrong with that last one")
    



# response = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# response.status_code
