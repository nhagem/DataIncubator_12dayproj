from flask import Flask, render_template, request, redirect
import requests
import quandl
import pandas as pd
from io import StringIO
from bokeh.plotting import figure, output_file, save
from bokeh.embed import components
from datetime import datetime

app = Flask(__name__)

def get_plot(df):
  output_file('plot.html')
  p = figure(x_axis_label='Date',y_axis_label='Close',x_axis_type="datetime")
  p.line(df['Date'],df['Close'], line_width=2)
  return(p)

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
  df['Date'] = pd.to_datetime(df['Date'])

  #df_sub = df[(df['Date'].dt.year==2017) & (df['Date'].dt.month==10)]

  p = get_plot(df)

  script, div = components(p)

  return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
  app.run(port=33507)
