import json
import requests
from bs4 import BeautifulSoup
import re


class Checking_skills:
    def __init__(self, skills, exp_level):
        self.skills = set(skills)
        self.exp_level = exp_level

    @staticmethod
    def get_html(url):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/112.0.0.0 Safari/537.36"
        }
        req = requests.get(url, headers=headers)
        src = req.text
        with open("data/vacance.html", "w", encoding='utf-8') as file:
            file.write(src)

    def parcing_sort(self):
        with open('data/profesia_sk_data.json', 'r') as f:
            data = json.load(f)
            f.close()
        new_data = []
        for i in data:
            name = i["Name"]
            if self.exp_level.lower() in name.lower().split():
                new_data.append(i)
            else:
                continue
        checked_data = []
        for i in new_data:
            url = i["Href"]
            Checking_skills.get_html(url)
            with open("data/vacance.html") as file:
                src = file.read()
            soup = BeautifulSoup(src, "lxml")
            vacancy_info = soup.find("main", class_="col-sm-8")
            vacancy_info = str(vacancy_info)
            vacancy_info.lower()
            words = (word.lower() for word in re.findall(r'\w+', vacancy_info))
            found_words = self.skills.intersection(words)
            if found_words != set():
                checked_data.append(i)
            else:
                continue
        with open("data/checked_profesia_sk_data.json", "a", encoding="utf-8") as file:
            file.truncate(0)
            json.dump(checked_data, file, indent=4, ensure_ascii=False)
            file.close()


def get_result(skills, exp_level):
    a = Checking_skills(skills, exp_level)
    a.parcing_sort()
