from flask import Flask, request, redirect, render_template
import cgi

#template_dir = os.path.join(os.path.dirname(__file__),
    #'templates')
#jinja_env = jinja2.Environment(
#loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/", methods=['POST'])
def validate_form():
    user = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_error = ''
    pass_error = ''
    verify_error = ''
    email_error = '' 

    if user == '':
        user_error = 'Please enter a username.'
    elif len(user) <3 or len(user) > 20:
        user_error = 'Please enter a valid username.'

    if password == '':
        pass_error = 'Please enter a password.'
    
    elif len(password) < 3 or len(password) > 20:
        pass_error = 'Please enter a valid password.'
        
    elif ' ' in password:
        pass_error = 'Letters and numbers only!'
    
    if verify != password:
        verify_error = 'Those passwords do not match.'

    if email:
        if '@' and '.' not in email:
            email_error = 'Please enter a valid email address.'
        if ' ' in email:
            email_error = 'No spaces allowed.'
        if len(email) <3 or len(email) > 20:
            email_error = 'Please enter a valid email address.'

    if len(user_error) > 0 or len(pass_error) > 0 or len(verify_error) > 0 or len(email_error) > 0:
         return render_template('signup_form.html', user_error=user_error, 
            pass_error=pass_error,
            verify_error=verify_error,
            email_error=email_error)
        #user_name = str(username)
    #redirect('/welcome?user_name={0}'.format(username))
    else:
        return render_template('welcome.html', username=user)

       


#@app.route("/welcome")
#def welcome():
    #template = jinja_env.get_template('welcome.html')
    #username = request.args.get['username']
    #return template.render(name=username)

app.run()