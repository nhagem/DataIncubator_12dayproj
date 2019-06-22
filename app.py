from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/graph', methods=['GET', 'POST'])
def graph():
  return render_template('about.html')
  pass

if __name__ == '__main__':
  app.run(port=33507)
