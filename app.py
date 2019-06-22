from flask import Flask, render_template, request, redirect
import requests
import quandl
import pandas as pd
from io import StringIO

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
  
  #Pull the requested data into a pandas dataframe
  df = pd.read_csv(StringIO(r.text),sep=',')


  return """
  <h1>Let it Burn</h1>
  <p>Talking to Quandl is {args}</p>
  """.format(args=df.head())

if __name__ == '__main__':
  app.run(port=33507)
