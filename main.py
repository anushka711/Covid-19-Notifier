from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
header = {"User-Agent":"Mozilla"}
r = Request("https://www.worldometers.info/coronavirus/country/india/",headers = header)
html = urlopen(r)
obj = bs(html,"html.parser")

new_cases = obj.find("li",{"class":"news_li"}).strong.text.split()[0]
new_deaths =list(obj.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

notifier=ToastNotifier()
message = new_cases +" new cases of Covid-19 today\nINDIA"
notifier.show_toast(title="Covid-19 Update",msg=message,duration=5)