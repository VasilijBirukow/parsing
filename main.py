from time import sleep
import requests
from bs4 import BeautifulSoup
import fake_headers


def gen_headers():
    headers_gen = fake_headers.Headers(os="win", browser="yandex")
    return headers_gen.generate()


url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"

response = requests.get(url, headers=gen_headers())
# print(response)
#
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
tag_main = soup.find("main", class_="vacancy-serp-content")
# print(tag_main)
job_openings = soup.find_all("div", class_="serp-item serp-item_link")
for vacancy in job_openings:
    d = vacancy_description.find("div", class_="g-user-content").text
    if "Django" in d or "Flask" in d:
        vacancy_description = vacancy.find("div", class_="vacancy-serp-item-body__main-info")
        link = str(vacancy_description.find("a", class_="bloko-link")["href"]).split("?")[0]
        company = vacancy_description.find("div", class_="vacancy-serp-item__meta-info-company").text
        city = vacancy_description.find("div", {"date_qa": "vacancy-serp__vacancy-address"}).text
        mony = vacancy_description.find("span", {"date_qa": "vacancy-serp__vacancy-compensation"}).text
        d = vacancy_description.find("div", class_="g-user-content").text

