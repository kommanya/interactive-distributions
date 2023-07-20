from dash import Dash, dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import i18n

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure() 
fig5 = go.Figure()
fig6 = go.Figure() 

def render(app:Dash)-> html.Div:
    return html.Div(id='Div_Weibull', children=[
         dbc.Row([
            dbc.Col([
                html.Div(i18n.t("labels.weibull CDF")), 
                dcc.Graph(
                id='Graph17',
                figure=fig1
                )],
                width={"size": 12},
                ),
            dbc.Col([
                html.Div(i18n.t("labels.weibull PDF")), 
                dcc.Graph(
                id='Graph18',
                figure=fig2
                )],
                width={"size": 12},
                )
            ]),
             dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_weibull-slider", min=-10, max=10, step=0.1, 
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
                                i18n.t("components.shape"),
                                dcc.Slider(id="shape-slider", min=0.1, 
                                max=10, step=0.1, value=1,
                                marks={0.1: {'label': '0.1'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=3),
                dbc.Col(children=[
                                i18n.t("components.scale"),
                                dcc.Slider(id="scale_weibull-slider", min=0.1, 
                                max=10, step=0.1, value=1,
                                marks={0: {'label': '0.1'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=3),
            ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.weibull CDF")), 
            dcc.Loading(dcc.Graph(id='Graph19',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.weibull PDF")), 
            dcc.Loading(dcc.Graph(id='Graph20',figure=fig4), type='cube')])
        ]),
        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.weibull CDF")), 
            dcc.Loading(dcc.Graph(id='Graph21',figure=fig5), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.weibull PDF")), 
            dcc.Loading(dcc.Graph(id='Graph22',figure=fig6), type='cube')])
        ])
    ])
  