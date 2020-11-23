from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
  app.run(debug=True)
