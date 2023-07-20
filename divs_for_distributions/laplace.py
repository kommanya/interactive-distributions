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
    return html.Div(id='Div_Laplace', children=[
        dbc.Row([
            dbc.Col([
                html.Div(i18n.t("labels.laplace CDF")), 
                dcc.Graph(
                id='Graph33',
                figure=fig1
                )],
                width={"size": 12},
                ),
            dbc.Col([
                html.Div(i18n.t("labels.laplace PDF")), 
                dcc.Graph(
                id='Graph34',
                figure=fig2
                )],
                width={"size": 12},
                )
            ]),

          dbc.Row([
            dbc.Col(children=[
                            i18n.t("components.shift"),
                            dcc.Slider(id="shift-slider", min=-5, 
                            max=5, step=0.1, value=0,
                            marks={-5: {'label': '-5'},
                            0: {'label': '0'},
                            5: {'label': '5'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6),
            dbc.Col(children=[
                            i18n.t("components.scale"),
                            dcc.Slider(id="scale_laplace-slider", min=0.1, 
                            max=5, step=0.1, value=1,
                            marks={0.1: {'label': '0.1'},
                            2.5: {'label': '2.5'},
                            5: {'label': '5'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6)
        ]),

        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.laplace CDF")), 
            dcc.Loading(dcc.Graph(id='Graph35',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.laplace PDF")), 
            dcc.Loading(dcc.Graph(id='Graph36',figure=fig4), type='cube')])
        ]),
        dbc.Row([
            dbc.Col(children=[
            html.Div(i18n.t("labels.laplace CDF")), 
            dcc.Loading(dcc.Graph(id='Graph37',figure=fig5), type='cube')]),
            dbc.Col(children=[
            html.Div(i18n.t("labels.laplace PDF")), 
            dcc.Loading(dcc.Graph(id='Graph38',figure=fig6), type='cube')])
        ]),

        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_laplace-slider", min=-10, max=10, step=0.1, 
                value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        )
    ])
