from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


driver = webdriver.Firefox()
driver.get("http://www.city-data.com//advanced/search.php#body?fips=0&csize=l&sc=2&sd=1&states=ALL&near=&nam_crit1=1033&b1033=MIN&e1033=MAX&i1033=0&nam_crit2=1027&b1027=MIN&e1027=MAX&i1027=0&ps=20&p=0")

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "norm")))

html = driver.page_source
get_data = BeautifulSoup(html, "lxml")
table = get_data.find_all("table", attrs={"id": "sr"})
print(table)