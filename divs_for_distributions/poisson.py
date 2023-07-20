from dash import Dash, dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import i18n

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure()

def render(app:Dash)-> html.Div:
    return html.Div(id='Div_Poisson', children=[
        dbc.Row([
            dbc.Col([
                html.Div(i18n.t("labels.poisson CDF")), 
                dcc.Graph(
                id='Graph13',
                figure=fig1
                )],
                width={"size": 12},
                ),
            dbc.Col([
                html.Div(i18n.t("labels.poisson PDF")), 
                dcc.Graph(
                id='Graph14',
                figure=fig2
                )],
                width={"size": 12},
                )
            ]),
        dbc.Row([
            dbc.Col(children=[
                'k',
                dcc.Slider(id="occurrences", min=0, max=50, step=1, value=5,
                                marks={0: {'label': '0'},
                                10: {'label': '10'},
                                20: {'label': '20'},
                                30: {'label': '30'},
                                40: {'label': '40'},
                                50: {'label': '50'}},
                                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ]),
        
        dbc.Row([
                dbc.Col(children=[
                                i18n.t("components.lambda"),
                                dcc.Slider(id="lambda-slider", min=0.1, 
                                max=50, step=1, value=5,
                                marks={0.1: {'label': '0.1'},
                                10: {'label': '10'},
                                20: {'label': '20'},
                                30: {'label': '30'},
                                40: {'label': '40'},
                                50: {'label': '50'},
                                },
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
        ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.poisson CDF")), 
            dcc.Loading(dcc.Graph(id='Graph15',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.poisson PDF")), 
            dcc.Loading(dcc.Graph(id='Graph16',figure=fig4), type='cube')])
        ])
    ])
    