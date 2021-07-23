import numpy as np
import pandas as pd
import requests
from urllib.request import urlopen
import json
import plotly.express as px
#import plotly.graph_objs as go

def cleandata(key_path):
    """call and clean covidactnow api results

    Args:
        None

    Returns:
        None

    """    
    
    #retrieve saved key provided by https://apidocs.covidactnow.org/ 
    with open(key_path) as file:
        key = file.read()

    Call_URL = 'https://api.covidactnow.org/v2/counties.json?apiKey=' + key

    response = requests.get(Call_URL)
    data = response.json()
    
    lst = []

    for i in range(len(data)):
        lst.append([data[i]['lastUpdatedDate'],data[i]['state'],data[i]['fips'],data[i]['actuals']['cases'],\
                    data[i]['county'], data[i]['metrics']['vaccinationsCompletedRatio'],\
                    data[i]['population'], data[i]['actuals']['newCases'], data[i]['actuals']['vaccinationsCompleted']])
    
    df = pd.DataFrame(lst, columns = ['last_updated_date','state','fips','cases',\
                                      'county', 'vaccines_completed_ratio', 'population', \
                                      'new_cases', 'vaccines_completed'])
    
    df = pd.DataFrame(lst, columns = ['last_updated_date','state','fips','cases', 'county', 'vaccines_completed_ratio', 'population','new_cases', 'vaccines_completed'])
    df['population'] = df['population'].map('{:,.0f}'.format)
    #df['cases'] = df['cases'].map('{:,.0f}'.format)
    #df['new_cases'] = df['new_cases'].map('{:,.0f}'.format)
    #df['vaccines_completed'] = df['vaccines_completed'].map('{:,.0f}'.format)
    df['vaccines_completed_ratio'] = df['vaccines_completed_ratio'] * 100.00  
    
    return df

def return_figures():
    """Creates 3 plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the 3 plotly visualizations

    """
    df = cleandata('data/config.txt')
    
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    
    fig_one = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='vaccines_completed_ratio',
                               color_continuous_scale="Viridis",
                               range_color=(0, 100),
                               mapbox_style="carto-positron",
                               hover_name="county",
                               hover_data=["state", "population"],
                               zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                               opacity=0.5,
                               labels={'vaccines_completed_ratio':'fully vaccinated rate'})
    fig_two = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='new_cases',
                           color_continuous_scale="temps",
                           range_color= (0, max(df['new_cases'])),
                           mapbox_style="carto-positron",
                           hover_name="county",
                           hover_data=["state", "population"],
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'new_cases':'new COVID-19 cases'}
                          )
    fig_three = px.choropleth_mapbox(df, geojson=counties, locations='fips', color='cases',
                           color_continuous_scale="reds",
                           range_color= (0, max(df['cases'])),
                           mapbox_style="carto-positron",
                           hover_name="county",
                           hover_data=["state", "population"],
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'cases':'cumulative COVID-19 cases'}
                          )
                      
    figures = []
    figures.append(fig_one.to_dict())
    figures.append(fig_two.to_dict())
    figures.append(fig_three.to_dict())

    return figures
    
def return_lastupdated():
    
        """Pulls last updated date from api

    Args:
        None

    Returns:
        string: last updated date

    """
    
    df = cleandata('data/config.txt')
    lastupdated = max(df['last_updated_date'])
    return lastupdated
