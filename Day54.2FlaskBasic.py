from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"

# Navigating to different pages
@app.route('/bye')
def bye():
    return "<p>Bye</p>"

# Acessing variable url
@app.route('/<users_name>')
def user(users_name):
    return f'Hello there: {users_name}!'

# Creating variable paths and converting the path to a specified data type
@app.route('/username/<name>/<int:number>')
def great(name, number):
    return f'Hello there {name}, you are {number} years old!'
    

if __name__ == '__main__':
    # Debug=True allows rerendring of website for any active change and activates debugger
    app.run(debug=True)