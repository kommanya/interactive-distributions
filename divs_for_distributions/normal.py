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
    return html.Div(id='Div_Normal', children=[
        dbc.Row([
            dbc.Col([
                html.Div(i18n.t("labels.norm CDF")), 
                dcc.Graph(
                id='Graph1',
                figure=fig1
                )],
                width={"size": 12},
            ),
            dbc.Col([
                html.Div(i18n.t("labels.norm PDF")), 
                dcc.Graph(
                id='Graph2',
                figure=fig2
                )],
                width={"size": 12},
            )
        ]),

        dbc.Row([
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_normal-slider", min=-10, max=10, step=0.1, 
                value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12})
        ]),

        dbc.Row([
                dbc.Col(children=[
                                i18n.t("components.mean"),
                                dcc.Slider(id="mean-slider", min=-5, 
                                max=5, step=0.1, value=0,
                                marks={-5: {'label': '-5'},
                                0: {'label': '0'},
                                5: {'label': '5'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6),
                dbc.Col(children=[
                                i18n.t("components.std"),
                                dcc.Slider(id="std-slider", min=0.1, 
                                max=10, step=0.1, value=1,
                                marks={0.1: {'label': '0.1'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
        ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.norm CDF")), 
            dcc.Loading(dcc.Graph(id='Graph3',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.norm PDF")), 
            dcc.Loading(dcc.Graph(id='Graph4',figure=fig4), type='cube')])
        ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.norm CDF")), 
            dcc.Loading(dcc.Graph(id='Graph5',figure=fig5), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.norm PDF")), 
            dcc.Loading(dcc.Graph(id='Graph6',figure=fig6), type='cube')])
        ]),
    ])
    