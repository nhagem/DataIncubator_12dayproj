from flask import Flask, render_template, request, redirect
import requests
import quandl
import pandas as pd
from io import StringIO
from bokeh.plotting import figure, output_file
from bokeh.embed import components

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


  p = figure(x_axis_label='Date',y_axis_label=request.args['features'])
  p.line(df_sub['Date'],df_sub[request.args['features']], line_width=2)

  script, div = components(p)

  return '<h1>Yeah okay</h1>'

  #return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
