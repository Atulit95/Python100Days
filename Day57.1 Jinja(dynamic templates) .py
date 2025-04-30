from flask import Flask, render_template
import random
import datetime as dt
 
app = Flask(__name__)
 


@app.route('/')
def hello_world():
    random_number = random.randint(1, 10)
    curr_year = dt.datetime.now().year
    return render_template('index3.html', num= random_number, year=curr_year, devloper= 'Knight')



if __name__ == '__main__':
    app.run(debug=True)