from dash import Dash, dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import i18n

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure() 

def render(app:Dash)-> html.Div:
    return html.Div(id='Div_Expon', children=[
        dbc.Row([
            dbc.Col([
                html.Div(i18n.t("labels.exp CDF")), 
                dcc.Graph(
                id='Graph29',
                figure=fig1
                )],
                width={"size": 12},
                ),
            dbc.Col([
                html.Div(i18n.t("labels.exp PDF")), 
                dcc.Graph(
                id='Graph30',
                figure=fig2
                )],
                width={"size": 12},
                )
            ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.exp CDF")), 
            dcc.Loading(dcc.Graph(id='Graph31',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.exp PDF")), 
            dcc.Loading(dcc.Graph(id='Graph32',figure=fig4), type='cube')])
        ]),

        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_expon-slider", min=-10, max=10, step=0.1, 
                value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),
        
        dbc.Row([
                dbc.Col(children=[
                                i18n.t("components.scale"),
                                dcc.Slider(id="scale_expon-slider", min=0.1, 
                                max=5, step=0.1, value=1,
                                marks={0.1: {'label': '0.1'},
                                1: {'label': '1'},
                                2: {'label': '2'},
                                3: {'label': '3'},
                                4: {'label': '4'},
                                5: {'label': '5'},
                                },
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
        ])
    ])
   