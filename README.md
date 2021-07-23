# COVID-19-Dashboard

My intentions are to use the visuals created by plotly using the covidactnow api to a dashboard hosted on Heroku for my family, friends and I to use.
I want to see if areas where outbreaks are still happening have low vaccination rates as well as see if areas that were affected the most cumulatively now have higher vaccination rates than others.

## Table of contents
* [Results](#results)
* [Acknowledgements](#acknowledgements)
* [Technologies](#technologies)
* [Libraries](#libraries)
* [Files](#files)
* [TODO](#todo)


# Results
<img width="1431" alt="Untitled 2" src="https://user-images.githubusercontent.com/33467922/126736374-d59b1170-2fe3-430d-b852-d5d99dbe5a91.png">
<img width="1373" alt="Untitled 3" src="https://user-images.githubusercontent.com/33467922/126736433-2b7a5e75-3bab-4a4e-baab-a71a7a2be37e.png">
<img width="1386" alt="Untitled 4" src="https://user-images.githubusercontent.com/33467922/126736481-eb1baf56-57bd-402e-a80d-83d807a6acfd.png">

# Acknowledgements
https://apidocs.covidactnow.org/

# Technologies
* Python 3.6
* Html
* Javascript

# Libraries

```
import numpy as np
import pandas as pd
import requests
from urllib.request import urlopen
import json
import plotly.express as px
from flask import render_template
```

```
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha384-tsQFqpEReu7ZLhBV2VZlAu7zcOV+rXbYlF2cqB8txI/8aZajjp4Bqd+V6D5IgvKT" crossorigin="anonymous"></script> 
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```

# Files
* index.html: contains html and javascript to render web page and plot graphs from plotly json
* routes.py: use flask to render template and send in python variables for javascript access
* wrangle_data.py: request latest date covidactnow api data with key and render plotly choropleth maps for vaccination rate, new cases and cumulative cases

# TODO
* Fix left margin of header and subheader
* Test making the graphs fluid
* Remove the the line app.run(host='0.0.0.0', port=3001, debug=True) in the myapp.py file before deploying to Heroku
* Create requirements txt file with all python libraries that Heroku will need
* Make sure the Procfile contains the line web gunicorn myapp:app
* Create private GIT to host app (because of api key) and deploy to Heroku

