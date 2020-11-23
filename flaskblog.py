from flask import Flask
app = Flask(__name__)

@app.route("/") #rootpage
@app.route("/home") #homepage which is same as root
def home():
  return "<h1>Home Page</h1>"

@app.route("/about") #about page
def about():
  return "<h1>About Page</h1>"

if __name__ == '__main__':
  app.run(debug=True)
