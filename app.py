from flask import Flask, render_template, request, redirect
import requests
import quandl
import pandas as pd
from io import StringIO
from bokeh.embed import components 
from bokeh.charts import Line

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
  df_sub = df[['Date',request.args['features']]]

  p = Line(df_sub, x='Date', y=request.args['features'], xlabel='Date', ylabel=request.args['features'])
  script, div = components(p)

  return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
