from flask import Flask, render_template
 
app = Flask(__name__)

# To render html files or other they need to be inside 'templates' folder
# But for static files likes images,css files,etc they need to be under folder named as 'static'.
 
@app.route('/')
def home():
    return render_template("cv_template.html")



if __name__ == '__main__':
    app.run(debug=True)