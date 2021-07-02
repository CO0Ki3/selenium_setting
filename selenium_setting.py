from selenium import webdriver

def driver_link():
  return (r'C:\Users\co0ki3\Desktop\Python\Selenium\chromedriver_win32\chromedriver.exe')

dv = webdriver.Chrome(driver_link())

def driver_site(n):
  return dv.get(n)