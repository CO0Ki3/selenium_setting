from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

dv = webdriver.Chrome(r'C:\Users\co0ki3\Desktop\Python\Types\Selenium\chromedriver_win32\chromedriver.exe')
dv.get("https://www.google.com")

input_box = dv.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys(input("Input: "))
input_box.send_keys(Keys.RETURN)

html = dv.page_source
soup = BeautifulSoup(html, 'html.parser')
head_text = soup.select('.LC20lb')

for i in head_text:
  print(i.text.strip())