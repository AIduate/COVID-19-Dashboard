from myapp import app
import json, plotly
from flask import render_template
from wrangling_scripts.wrangle_data import return_figures, return_lastupdated

@app.route('/')
@app.route('/index')

def index():

    figures = return_figures()

    # plot ids for the html id tag
    ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

    # Convert the plotly figures to JSON for javascript in html template
    figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)
    
    last_updated_date = return_lastupdated()

    return render_template('index.html',
                           ids=ids,
                           figuresJSON=figuresJSON,
                          last_updated_date=last_updated_date)
