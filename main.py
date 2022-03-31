from flask import *
import smtplib

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'myemail@gmail.com'
app.config['MAIL_PASSWORD'] = 'helloworld'
app.config['MAIL_USE_SSL'] = True


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about')
@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog')
@app.route('/blog.html')
def blog():
    return render_template('blog.html')


@app.route('/blog-details')
@app.route('/blog-details.html')
def blog_detail():
    return render_template('blog-details.html')


@app.route('/contact')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/service')
@app.route('/service.html')
def service():
    return render_template('service.html')


@app.route('/send_mail', methods=['POST'])
def send_mail():
    finame = request.form['first_name']
    sename = request.form['last_name']
    subject = request.form['subject']
    name = finame + ' ' + sename
    email = request.form['email']
    message = request.form['message']
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # region Login
        smtp.login('kimlong101020@gmail.com', 'KimLong10102030')
        # endregion
        subject = subject
        body = "Guess name: " + name + "\nEmail: " + email + "\n" + "Message: " + message
        # body = u' '.join((name, email, message)).encode('utf-8').strip()
        # body = r.join((name, '\n', email, '\n', message)).encode('utf-8').strip()
        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8').strip()
        smtp.sendmail('kimlong101020@gmail.com', 'longdnk18@uef.edu.vn', msg)
    return redirect(url_for('index'))


@app.route('/subcribe', methods=['POST'])
def subcribe():
    email = request.form['email']
    name = email + ' '
    message = 'Hello i\'m ' + email + ' please add me'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        # region Login
        smtp.login('kimlong101020@gmail.com', 'KimLong10102030')
        # endregion
        subject = name + " " + "request"
        body = "Guess name: " + name + "\nEmail: " + email + "\n" + "Message: " + message
        # body = u' '.join((name, email, message)).encode('utf-8').strip()
        # body = r.join((name, '\n', email, '\n', message)).encode('utf-8').strip()
        msg = f'Subject: {subject}\n\n{body}'.encode('utf-8').strip()
        smtp.sendmail('kimlong101020@gmail.com', 'longdnk18@uef.edu.vn', msg)
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(debug=True)
