# COVID-19-Dashboard

I want to use this web app dashboard from friends, family and myself to examine if areas where outbreaks are still happening have low vaccination rates as well as see if areas that were affected the most cumulatively now have higher vaccination rates than others.

## Table of contents
* [Results](#results)
* [Acknowledgements](#acknowledgements)
* [Technologies](#technologies)
* [Libraries](#libraries)
* [Files](#files)

# Results
https://amanda-covid-web-app.herokuapp.com/
<img width="1431" alt="Untitled 5" src="https://user-images.githubusercontent.com/33467922/126781615-689c8a97-5bac-4802-ad9e-4d460529efae.png">

# Acknowledgements
https://apidocs.covidactnow.org/
https://plotly.com/python/choropleth-maps/
https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5

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
from decouple import config
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


