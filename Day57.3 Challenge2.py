
# ------------- Hosting Part----------- 

from flask import Flask, render_template
import requests

app = Flask(__name__)
 
@app.route('/')
def deatils_page():
    return '<p>Type your to Url like: 12.0.0.1/guess/"your name"</p>'

@app.route('/blog')
def guess_details():
    data = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("index5.html", blog_posts=data)

@app.route('/blog/<int:number>')
def guess_id3_details(number):
    data = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391').json()
    return render_template("index5.html", blog_posts=[data[number-1]])


if __name__ == '__main__':
    app.run(debug=True)