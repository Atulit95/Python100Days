from flask import Flask, render_template
import requests

def api_handler():
     blog_api_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
     return blog_api_response    

app = Flask(__name__)
 
@app.route('/')
def home_page():
    blog_data = api_handler()
    return render_template('capstone_index.html',blogs=blog_data)

@app.route('/post/<int:id>')
def article_page(id):
    blog_data =api_handler()
    return render_template('capstone_post.html', blog=blog_data[id-1],)   


if __name__ == '__main__': 
    app.run(debug=True)