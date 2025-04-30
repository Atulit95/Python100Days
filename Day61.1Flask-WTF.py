from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5
 
app = Flask(__name__)
app.secret_key = 'any-string-you-want-just-dont-tell-anyone'
bootstrap = Bootstrap5(app)

# Form Creation
class MyForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired(), Email(message='Invalid Email Address') ])
    password = PasswordField(label='password', validators=[DataRequired(),Length(min=8, message='Field must be 8 character long.')])
    submit = SubmitField(label="login")

@app.route('/')
def home_page():
    return render_template('day61/index.html')

@app.route('/login_page',methods=['GET','POST'])
def login_page():
    form = MyForm()
    print(form.password.data)
    if form.validate_on_submit():
        if form.email.data=='admin@email.com' and form.password.data=='12345678':
            return render_template('day61/success.html')
        else:
            return render_template('day61/denied.html')
    return render_template('day61/login.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)