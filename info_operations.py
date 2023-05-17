import json


def read_info():
    with open("data/client_info.txt", "r") as file:
        city = file.readline().strip()
        exp_level = file.readline().strip()
        find = file.readline().strip()
        skills = file.readline().strip()
    data = {'exp_level': exp_level, 'skills': skills, 'city': city, 'find': find}
    return data


def return_vacancies():
    with open('data/response.json', 'r') as f:
        data = json.load(f)
    all_vacansies = ''
    counter = 1
    for i in data:
        vacansies = 'Вакансія №: ' + str(counter) + "\n"
        vacansies = vacansies + 'Назва вакансії: ' + i['Name'] + "\n"
        vacansies = vacansies + 'Працедавець: ' + i['Employer'] + "\n"
        vacansies = vacansies + 'Зарплатня: ' + i['Salary'] + "\n"
        vacansies = vacansies + 'Посилання на вакансію: ' + i['Href'] + "\n"
        all_vacansies = all_vacansies + vacansies
        counter = counter + 1
    return all_vacansies
