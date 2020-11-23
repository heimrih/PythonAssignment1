from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'abc123'

posts = [
  {
    'author': 'Wei Lun',
    'title': 'My first Post',
    'content': 'First Post body',
    'date_posted': 'November 20, 2020'
  },
  {
    'author': 'Chong Meng',
    'title': 'My second Post',
    'content': 'Second Post body stuffs',
    'date_posted': 'November 20, 2020'
  }
]

@app.route("/") #rootpage
@app.route("/home") #homepage which is same as root
def home():
  return render_template('home.html', posts=posts)

@app.route("/about") #about page
def about():
  return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash('Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
  app.run(debug=True)
