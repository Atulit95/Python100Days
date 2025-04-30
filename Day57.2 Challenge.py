from flask import Flask, render_template
import requests
# ------------ Getting data to render from API ------------------
def api_responses(name):
    agify_api_response = requests.get(url="https://api.agify.io", params={"name":name})
    genderize_api_response = requests.get(url="https://api.genderize.io", params={"name":name})
    gender_data = genderize_api_response.json()['gender']
    age_data = agify_api_response.json()['age']
    return {"age": age_data, "gender": gender_data}
    
# print(api_responses("Angela"))   # Check functionality


# ------------- Hosting Part----------- 

app = Flask(__name__)
 
@app.route('/')
def deatils_page():
    return '<p>Type your to Url like: 12.0.0.1/guess/"your name"</p>'

@app.route('/guess/<name>')
def guess_details(name):
    data = api_responses(name)
    return render_template("index4.html", user=name, gender=data['gender'], age=data['age'])


if __name__ == '__main__':
    app.run(debug=True)