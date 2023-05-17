from flask import Flask, request, jsonify
import json
import parcing_part
import sort_by_skills

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    # data = {'exp_level': 'junior', 'skills': ("spring", "maven"), 'city': 'Bratislava', 'find': 'java programmer'}
    exp_level = data['exp_level']
    skills = data['skills']
    city = data['city']
    find = data['find']
    parcing_part.get_info(str(city), 30, str(exp_level) + "+" + str(find))
    sort_by_skills.get_result(skills, exp_level)
    with open('data/checked_profesia_sk_data.json', 'r', encoding="utf-8") as f:
        prepared_data = json.load(f)
    f.close()
    return jsonify(prepared_data)


if __name__ == '__main__':
    app.run()
