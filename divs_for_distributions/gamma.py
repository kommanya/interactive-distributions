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
    return html.Div(id='Div_Gamma', children=[
        dbc.Row([
            dbc.Col([
                html.Div(i18n.t("labels.gamma CDF")), 
                dcc.Graph(
                id='Graph23',
                figure=fig1
                )],
                width={"size": 12},
                ),
            dbc.Col([
                html.Div(i18n.t("labels.gamma PDF")), 
                dcc.Graph(
                id='Graph24',
                figure=fig2
                )],
                width={"size": 12},
                )
            ]),

        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_gamma-slider", min=0, max=20, step=0.1, 
                value=[0,1],
                marks={0: {'label': '0'},
                10: {'label': '10'},
                20: {'label': '20'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),

        dbc.Row([
            dbc.Col(children=[
                            i18n.t("components.k"),
                            dcc.Slider(id="a-slider", min=0.1, 
                            max=10, step=0.1, value=1,
                            marks={0.1: {'label': '0.1'},
                            5: {'label': '5'},
                            10: {'label': '10'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6),
            dbc.Col(children=[
                            i18n.t("components.tetta"),
                            dcc.Slider(id="tetta-slider", min=0.1, 
                            max=10, step=0.1, value=1,
                            marks={0.1: {'label': '0.1'},
                            5: {'label': '5'},
                            10: {'label': '10'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6)
        ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.gamma CDF")), 
            dcc.Loading(dcc.Graph(id='Graph25',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.gamma PDF")), 
            dcc.Loading(dcc.Graph(id='Graph26',figure=fig4), type='cube')])
        ]),
        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.gamma CDF")), 
            dcc.Loading(dcc.Graph(id='Graph27',figure=fig5), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.gamma PDF")), 
            dcc.Loading(dcc.Graph(id='Graph28',figure=fig6), type='cube')])
        ])
    ])
