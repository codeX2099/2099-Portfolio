from flask import Flask, render_template, request,session
import re

app = Flask(__name__)
app.secret_key='Spiderman-2009'
@app.route('/')
def index():
    # Clear session data when the page is refreshed
    session.clear()
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    name = request.form['name']
    email = request.form['email']
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return 'The email id: {} is valid, Thank You For Your Coorperation {}'.format(email,name)
    else:
        return 'Unfortunately {}, the email address {} entered is not valid please try again'.format(name,email)


if __name__ == '__main__':
    app.run(debug=True)