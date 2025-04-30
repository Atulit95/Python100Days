from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('form.html')

@app.route("/login", methods=['GET'])
def recive_data():
    if request.method == 'GET':
        username = request.args.get('username')
    return f'<h1>{username}</h1>'


if __name__ == '__main__':
    app.run(debug=True)