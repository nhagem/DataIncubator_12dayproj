from flask import Flask, render_template, request, redirect
import requests
import quandl

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/graph', methods=['GET', 'POST'])
def graph():
  
  quandl.ApiConfig.api_key = "kbhrM4FS1yrozTefNaky"

  r = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/{stock}.csv'.format(stock=request.args['ticker']), auth=('natasha.hagemeyer@mg.thedataincubator.com', 'ahsataN1!'))

  return """
  <h1>Let it Burn</h1>
  <p>Talking to Quandl is {args}</p>
  """.format(args=r.text)

if __name__ == '__main__':
  app.run(port=33507)
