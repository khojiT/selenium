from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("user-data-dir=C:\\Users\\persian\\AppData\\Local\\Google\\Chrome\\User Data\\")
driver = webdriver.Chrome(executable_path=r'C:\Users\persian\Desktop\chromedriver.exe', chrome_options=options)
url = 'http://www.tsetmc.com/Loader.aspx?ParTree=15131F'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
r = soup.find_all('a', {'class': 'inst'})
l = []
for i in range(len(r)):
    if i % 2 ==0:
        l = l + [r[i].text]
