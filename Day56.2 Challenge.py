# try to change backgroud of index1.html using css file
from flask import Flask, render_template
 
app = Flask(__name__)

# Staic files are saved by the browser so even if we make change to the file and restart the server the browser still loads the old static file with old code/change but to load the current change we can use hard reload of browser i.e. (shift + refersh) which reloads all th file from server reseting its cache.

@app.route('/')
def home():
    return render_template("index1.html")



if __name__ == '__main__':
    app.run(debug=True)