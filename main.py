import content as content
import requests  #импортируем наш знакомый модуль
import lxml.html
from lxml import etree
html = requests.get('https://www.python.org/').content  #получим html главной странички официального сайта python

tree1 = etree.parse("Welcome to Python.org.html", lxml.html.HTMLParser()) # попытаемся спарсить наш файл с помощью html парсера
ul1 = tree1.findall("body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[1]")# помещаем в аргумент методу findall скопированный xpath

# создаём цикл в котором мы будем выводить название каждого элемента из списка
for li1 in ul1:
    a = li1.find('a') # в каждом элементе находим где хранится название. У нас это тег <a>
    time = li1.find('time')
    print(time.get('datetime'), a.text) # из этого тега забираем текст

tree2 = etree.parse("Welcome to Python.org.html", lxml.html.HTMLParser())
ul2 = tree2.findall("body/div/div[3]/div/section/div[2]/div[1]/div/ul/li[2]")
for li2 in ul2:
    a = li2.find('a')
    time = li2.find('time')
    print(time.get('datetime'), a.text)
