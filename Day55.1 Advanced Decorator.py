from flask import Flask

app = Flask(__name__)

# Complete three decorators below.
def make_bold(function):
    """It is used to bold the text"""
    def wrapper_function():
        text = function()
        return f'<b>{text}</b>'
    return wrapper_function
        
    
def make_emphasis(function):
    '''It is used to make the text emphasised'''
    def wrapper_function():
        text = function()
        return f'<em>{text}</em>'
    return wrapper_function
    

def make_underlined(function):
    '''It underlines the text.'''
    def wrapper_function():
        text = function()
        return f'<u>{text}</u>'
    return wrapper_function
    

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>"


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return '<h1 style="text-align:center">Bye!</h1>'

if __name__ == '__main__':
    # Debug=True allows rerendring of website for any active change and activates debugger
    app.run(debug=True)