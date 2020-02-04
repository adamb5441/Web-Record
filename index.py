from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import pdfkit

url = "https://libreboot.org/docs"
url2 = "https://vuetifyjs.com/en/"
url3 = "https://nodejs.org/en/docs/"
url4 = "https://docs.microsoft.com/en-us/dotnet/csharp/"
# print Single mage
def printpage(url):
    pdfkit.from_url(url, 'out.pdf')

# will step threw and print everything with route example: https://libreboot.org/docs/
def printContent(url):
    # while True:
    req = Request(url, headers={'User-Agent': 'chrome/79'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)
    print(links)

#this will prompt the user to select th content they want
def custom():
    print("custom")

printContent(url4)
