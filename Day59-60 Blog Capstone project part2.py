from flask import Flask, render_template, request
import requests
import smtplib

my_email = "your_mail"
my_password = "your_password"

def api_handler():
    blog_api_response = requests.get(url="https://api.npoint.io/674f5423f73deab1e9a7").json()
    return blog_api_response   

blog_response = api_handler()

app = Flask(__name__)
 
@app.route('/')
def home_page():
    return render_template('./capstone_part2/index.html', blogs=blog_response)

@app.route('/about_page')
def about_page():
    return render_template('/capstone_part2/about.html')

# -------------- Changes made during day60 to make form on contact page working ----------------------
@app.route('/contact_page', methods=['GET','POST'])
def contact_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
      
        # formatting is important for yahoo services
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        email_message = f"From: {my_email}\n"
        email_message += f"To: reciver's_mail\n"
        email_message += f"Subject: {subject}\n\n{body}"
        # -----------------------------------------------
        
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connections:
            connections.starttls()
            connections.login(user=my_email,password=my_password)
            connections.sendmail(
                from_addr=my_email,
                to_addrs="reciver_mail",
                msg=email_message
            )
        
        return render_template('/capstone_part2/contact.html', msg_sent=True)
    else:
        return render_template('/capstone_part2/contact.html', msg_sent=False)

# --------------------********------------------------

@app.route('/post/<int:id>')
def article_page(id):
    blog_data =api_handler()
    return render_template('/capstone_part2/post.html', blog=blog_data[id-1],)


if __name__ == '__main__':
    app.run(debug=True)