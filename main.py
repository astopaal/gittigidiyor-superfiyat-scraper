from selenium import webdriver
from bs4 import BeautifulSoup

DRIVER_PATH = "./msedgedriver.exe"

driver = webdriver.Edge(executable_path=DRIVER_PATH)
driver.get("https://www.gittigidiyor.com/")
source = driver.page_source

soup = BeautifulSoup(source, 'html.parser')

articles = soup.find_all("article", class_="sc-1n49x8z-0 zjojpt-1 faPHLI")

for i in articles:
     name = i.find("h2")
     print(name.text)
     price = i.find("span", class_="sc-1tdlrg-0 yf6n83-0 eCZVJO sc-1n2i5kn-3 cMKOHq")
     print(price.text)

