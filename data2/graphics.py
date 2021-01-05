import plotly.express as px
import pandas as pd

df1 = pd.read_csv("data2/worldwideattitude/FinaleDataAttitude.csv")
df2 = pd.read_csv("data2/worldwideattitude/test1.csv")

df3=  pd.merge(df1, df2, on="ISO")

def hist():
    histogram = px.histogram(df1, x = "COUNTRYR", y = "Q1_Consider_Living_CC", histfunc='avg',
                        animation_frame="GENDERF",
                            labels={
                            "COUNTRYR": "",
                            "Q1_Consider_Living_CC": "living climate change quesion"
                            })
    histogram.add_shape(type="line",
            x0=-0.5, y0=1, x1=29.5, y1=1,
            line=dict(
                color="lime",
                width=2,
                dash="dashdot")
            )
    histogram.update_layout(yaxis_range=[0,5])

    return histogram


def map():
    map = px.choropleth(df2, locations="ISO",
                            color="PUBLI_RATE",
                            hover_name="COUNTRY",
                            title='Public Opinion Worldwide',
                            color_continuous_scale=px.colors.sequential.Viridis,
                            )


def pie():
    colors1 = ['yellow', 'greenyellow', 'mediumseagreen', 'darkblue','indigo']

    piechart = go.Figure(data=[go.Pie( labels=['Yes, of course','Yes, a little','Not really','Not at all','Dont know'],
                                values = df1['Q1_Consider_Living_CC'].value_counts())])
    piechart.update_traces(hoverinfo='label+percent', textinfo='label',
                    marker=dict(colors=colors1, line=dict(color='#000000', width=0.5)))
    piechart.update_layout(title = "Do you consider we are living a Climate Change ?", title_font_size = 15, showlegend=False)

    return piechart
