import requests
from bs4 import BeautifulSoup
import json


class Profesia_sk:
    def __init__(self, city, metres, job):
        self.city = city
        self.metres = metres
        self.job = job

    def check_job(self):
        checked_job = self.job.strip()
        checked_job = checked_job.replace(" ", "+")
        if not all(ord(c) < 128 for c in checked_job):
            return 0
        else:
            return checked_job

    def get_info(self):
        url = "https://www.profesia.sk/praca/{0}/?radius=radius{1}&search_anywhere={2}".format(self.city, self.metres,
                                                                                               self.check_job())
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/112.0.0.0 Safari/537.36"
        }
        req = requests.get(url, headers=headers)
        src = req.text
        with open("data/index.html", "w", encoding='utf-8') as file:
            file.write(src)
            file.close()
        Profesia_sk.get_vacance()

    @staticmethod
    def get_vacance():
        with open("data/index.html") as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")
        vacancy_name = soup.find_all('li', class_='list-row')
        all_vacansies = []
        for vacancy in vacancy_name:
            title_elem = vacancy.find('h2')
            if title_elem is not None:
                title = title_elem.text
                all_vacansies.append({"Name": title})
        employers_names = soup.find_all('span', class_='employer')
        counter = 0
        for employer in employers_names:
            try:
                all_vacansies[counter].update({"Employer": employer.text})
            except:
                break
            counter += 1
        all_salary = soup.find_all('span', class_="label label-bordered green half-margin-on-top")
        counter = 0
        for salary in all_salary:
            all_vacansies[counter].update({"Salary": salary.text.strip()})
            counter += 1
        counter = 0
        vacancy_href = soup.find_all("li", class_="list-row")
        for href in vacancy_href:
            try:
                all_vacansies[counter].update(
                    {"Href": "https://www.profesia.sk" + href.find('h2').find("a").get("href")})
            except:
                continue
            counter += 1
        with open("data/profesia_sk_data.json", "a", encoding="utf-8") as file:
            file.truncate(0)
            json.dump(all_vacansies, file, indent=4, ensure_ascii=False)
            file.close()


def get_info(city, metres, job):
    a = Profesia_sk(city, metres, job)
    a.get_info()
