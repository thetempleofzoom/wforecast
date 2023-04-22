import streamlit as sl
import plotly.express as px
from apicall import call

sl.header('Weather Forecast for the next few days')

place = sl.text_input('Place', placeholder='type a city name')

days = sl.slider('# of forecast days:', min_value = 1,
                 max_value = 5)

dropdown = sl.selectbox('Select data to view:', ('Temperature', 'Cloud Cover'))



dates = []
values = []
images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
          'Snow': 'images/snow.png'}

if place:
    try:
        datapoints, contents = call(days, place)
        sl.subheader(f'{dropdown} for the next {days} days in '
             f'{place.title()}')
        dates = [contents[dtp]['dt_txt'] for dtp in range(0, datapoints, 1)]

        if dropdown == 'Temperature':
            values = [round(contents[dtp]['main']['temp'] / 10, 1) for dtp in range(0, datapoints, 1)]
            # use dir to see plotly methods
            figure = px.line(x=dates, y=values,
                             labels={'x': 'Date', 'y': 'Temperature (C)'})
            sl.plotly_chart(figure)
        else:
            values = [(contents[dtp]['weather'][0]['main']) for dtp in range(0, datapoints, 1)]
            pngs = [images[value] for value in values]
            sl.image(pngs, width=115, caption=dates)
            

    except KeyError:
        sl.markdown("**:red[Place doesn't exist!]**")



