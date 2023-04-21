import streamlit as sl
import plotly.express as px
from apicall import call

sl.header('Weather Forecast for the next few days')

place = sl.text_input('Place', placeholder='type a city name')

days = sl.slider('# of forecast days:', min_value = 1,
                 max_value = 5)

dropdown = sl.selectbox('Select data to view:', ('Temperature', 'Cloud Cover'))

sl.subheader(f'{dropdown} for the next {days} days in '
             f'{place.title()}')

#call function using days input
d, v = call(dropdown, days, place)

# use dir to see plotly methods
if dropdown == 'Temperature':
    figure = px.line(x=d, y= v,
                 labels={'x':'Date', 'y':'Temperature (C)'})
else:
    figure = px.line(x=d, y=v,
                     labels={'x': 'Date', 'y': 'Cloud Cover'})

sl.plotly_chart(figure)

