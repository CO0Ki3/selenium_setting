### Naver Webtoon Crawler
import selenium_setting
from bs4 import BeautifulSoup

selenium_setting.driver_site("https://comic.naver.com/webtoon/weekday.nhn")

dv = selenium_setting.dv

date_list = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]

input_date = int(input("input : "))
html = dv.page_source
soup = BeautifulSoup(html, 'html.parser')
date_webtoon_address = soup.find('h4', class_ = date_list[input_date]).parent
webtoon_name = date_webtoon_address.select('.title')

for i in webtoon_name:
  print(i.text.strip())
# for i in date_webtoon_address:
#   print(i.text.strip())
# # address = date_webtoon_address.page_source
# # soup = bs.find()
# # webtoon_name = soup.select('.title')

# # for i in webtoon_name:
# #   print(i.text.strip())
