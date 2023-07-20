from dash import Dash, dcc, html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import i18n

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure() 

def render(app:Dash)-> html.Div:
    return html.Div(id='Div_Gaussian_Mixture', children=[
        dcc.Store(id='weights', data=[]),
        dcc.Store(id='means', data=[]),
        dcc.Store(id='stds', data=[]),
        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_gaussian-slider", min=-10, max=10, step=0.1, 
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
                                i18n.t("components.mean"),
                                dcc.Slider(id="mean_gaussian-slider", min=-5, 
                                max=5, step=0.1, value=0,
                                marks={-5: {'label': '-5'},
                                0: {'label': '0'},
                                5: {'label': '5'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6),
                dbc.Col(children=[
                                i18n.t("components.std"),
                                dcc.Slider(id="std_gaussian-slider", min=0, 
                                max=10, step=0.1, value=1,
                                marks={0: {'label': '0'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
            ]),

        dbc.Row([
            dbc.Col([
                html.Div(i18n.t("components.input")),
                dcc.Input(
                id="input",
                type='number')
            ])
        ]),
        dbc.Row([
            dbc.Col(children=[
                html.Button(i18n.t("components.add"), id='btn-add', n_clicks=0)
            ]),
            dbc.Col(children=[
                html.Button(i18n.t("components.clean"), id='btn-clean', n_clicks=0)
            ]),
        ]),
        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.gauss mixture CDF")), 
            dcc.Loading(dcc.Graph(id='Graph39',figure=fig1), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.gauss mixture PDF")), 
            dcc.Loading(dcc.Graph(id='Graph40',figure=fig2), type='cube')])
        ])
    ])