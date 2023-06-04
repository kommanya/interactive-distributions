from dash import Dash, dcc, html, ctx
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import scipy.stats as ss
import dash_bootstrap_components as dbc
import plotly.express as px

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY, dbc_css])



styles = {

    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()
fig4 = go.Figure()

app.layout = dbc.Container([
    dcc.Dropdown(['Normal', 'Uniform','Poisson','Weibull','Gamma','Exponential','Laplace','Gaussian Mixture'], 'Normal', 
                 id='distribution-dropdown'),

    html.Div(id='Div_Normal', children=[
        dbc.Row([
            dbc.Col(children=[
            html.Div('Normal CDF'), 
            dcc.Loading(dcc.Graph(id='Graph1',figure=fig1), type='cube')]),
            dbc.Col(children=[
            html.Div('Normal PDF'), 
            dcc.Loading(dcc.Graph(id='Graph2',figure=fig2), type='cube')])
        ]),
        dbc.Row([
            dbc.Col(children=[
            html.Div('Normal CDF'), 
            dcc.Loading(dcc.Graph(id='Graph17',figure=fig3), type='cube')]),
            dbc.Col(children=[
            html.Div('Normal PDF'), 
            dcc.Loading(dcc.Graph(id='Graph18',figure=fig4), type='cube')])
        ]),
        
        dbc.Row([
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_normal-slider", min=-10, max=10, step=0.1, value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ]),
        
       dbc.Row([
                dbc.Col(children=[
                                "mean-slider",
                                dcc.Slider(id="mean-slider", min=-5, 
                                max=5, step=0.1, value=0,
                                marks={-5: {'label': '-5'},
                                0: {'label': '0'},
                                5: {'label': '5'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6),
                dbc.Col(children=[
                                "std-slider",
                                dcc.Slider(id="std-slider", min=0, 
                                max=10, step=0.1, value=1,
                                marks={0: {'label': '0'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
            ]),
    ]),
    html.Div(id='Div_Uniform', children=[
        dbc.Row(
            dbc.Col(
                html.Div('Uniform CDF'),
                width={"size": 12, "offset": 6},
                )
            ),
        
        dcc.Graph(
            id='Graph3',
            figure=fig1
        ),

        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_uniform-slider", min=-10, max=10, step=0.1, value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),
        
        dbc.Row(
            dbc.Col(
                html.Div('Uniform PDF'),
                width={"size": 12, "offset": 6},
                )
            ),

        dcc.Graph(
            id='Graph4',
            figure=fig2
        ),

        dbc.Row([
            dbc.Col(children=[
                            'Left boundary slider',
                            dcc.Slider(id="left_boundary-slider", min=-5, 
                            max=5, step=0.1, value=0,
                            marks={-5: {'label': '-5'},
                            0: {'label': '0'},
                            5: {'label': '5'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6),
            dbc.Col(children=[
                            'Right boundary slider',
                            dcc.Slider(id="right_boundary-slider", min=-5, 
                            max=5, step=0.1, value=1,
                            marks={-5: {'label': '-5'},
                            0: {'label': '0'},
                            5: {'label': '5'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6)
        ])
    ]),
    html.Div(id='Div_Poisson', children=[
        dbc.Row([
            dbc.Col(
                html.Div('Poisson CDF'),
                width={"size": 12, "offset": 6},
                )
        ]),
        
        dcc.Graph(
            id='Graph5',
            figure=fig1
        ),

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
            dbc.Col(
                html.Div('Poisson PDF'),
                width={"size": 12, "offset": 6},
                )
        ]),

        dcc.Graph(
            id='Graph6',
            figure=fig2
        ),
        
        dbc.Row([
                dbc.Col(children=[
                                "lambda-slider",
                                dcc.Slider(id="lambda-slider", min=0, 
                                max=50, step=1, value=5,
                                marks={0: {'label': '0'},
                                10: {'label': '10'},
                                20: {'label': '20'},
                                30: {'label': '30'},
                                40: {'label': '40'},
                                50: {'label': '50'},
                                },
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
        ])
    ]),

    html.Div(id='Div_Weibull', children=[
     dbc.Row(
            dbc.Col(
                html.Div('Weibull CDF'),
                width={"size": 12, "offset": 6},
                )
            ),
        
        dcc.Graph(
            id='Graph7',
            figure=fig1
        ),
        
        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_weibull-slider", min=-10, max=10, step=0.1, value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),
        
        dbc.Row(
            dbc.Col(
                html.Div('Weibull PDF'),
                width={"size": 12, "offset": 6},
                )
            ),

        dcc.Graph(
            id='Graph8',
            figure=fig2
        ),
        
        dbc.Row([
                dbc.Col(children=[
                                "shape-slider",
                                dcc.Slider(id="shape-slider", min=0, 
                                max=10, step=0.1, value=1,
                                marks={0: {'label': '0'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=3),
                dbc.Col(children=[
                                "scale-slider",
                                dcc.Slider(id="scale_weibull-slider", min=0, 
                                max=10, step=0.1, value=1,
                                marks={0: {'label': '0'},
                                5: {'label': '5'},
                                10: {'label': '10'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=3),
            ]),
    ]),

    html.Div(id='Div_Gamma', children=[
        dbc.Row(
            dbc.Col(
                html.Div('Gamma CDF'),
                width={"size": 12, "offset": 6},
                )
            ),
        
        dcc.Graph(
            id='Graph9',
            figure=fig1
        ),

        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_gamma-slider", min=0, max=20, step=0.1, value=[0,1],
                marks={0: {'label': '0'},
                10: {'label': '10'},
                20: {'label': '20'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),
        
        dbc.Row(
            dbc.Col(
                html.Div('Gamma PDF'),
                width={"size": 12, "offset": 6},
                )
            ),

        dcc.Graph(
            id='Graph10',
            figure=fig2
        ),

        dbc.Row([
            dbc.Col(children=[
                            'a slider',
                            dcc.Slider(id="a-slider", min=0, 
                            max=10, step=0.1, value=1,
                            marks={0: {'label': '0'},
                            5: {'label': '5'},
                            10: {'label': '10'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6),
            dbc.Col(children=[
                            'tetta slider',
                            dcc.Slider(id="tetta-slider", min=0, 
                            max=10, step=0.1, value=1,
                            marks={0: {'label': '0'},
                            5: {'label': '5'},
                            10: {'label': '10'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6)
        ])
    ]),
    html.Div(id='Div_Expon', children=[
        dbc.Row(
            dbc.Col(
                html.Div('Exponential CDF'),
                width={"size": 12, "offset": 6},
                )
            ),
        
        dcc.Graph(
            id='Graph11',
            figure=fig1
        ),

        dbc.Row(
            dbc.Col(children=[
                'x',
                dcc.RangeSlider(id="x_expon-slider", min=-10, max=10, step=0.1, value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),

        dbc.Row(
            dbc.Col(
                html.Div('Exponential PDF'),
                width={"size": 12, "offset": 6},
                )
            ),

        dcc.Graph(
            id='Graph12',
            figure=fig2
        ),
        
        dbc.Row([
                dbc.Col(children=[
                                "scale-slider",
                                dcc.Slider(id="scale_expon-slider", min=0, 
                                max=5, step=0.1, value=1,
                                marks={0: {'label': '0'},
                                1: {'label': '1'},
                                2: {'label': '2'},
                                3: {'label': '3'},
                                4: {'label': '4'},
                                5: {'label': '5'},
                                },
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6)
        ])
    ]),
    html.Div(id='Div_Laplace', children=[
        dbc.Row(
            dbc.Col(
                html.Div('Laplace CDF'),
                width={"size": 12, "offset": 6},
                )
            ),
        
        dcc.Graph(
            id='Graph13',
            figure=fig1
        ),

        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_laplace-slider", min=-10, max=10, step=0.1, value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),
        
        dbc.Row(
            dbc.Col(
                html.Div('Laplace PDF'),
                width={"size": 12, "offset": 6},
                )
            ),

        dcc.Graph(
            id='Graph14',
            figure=fig2
        ),

        dbc.Row([
            dbc.Col(children=[
                            'shift',
                            dcc.Slider(id="shift-slider", min=-5, 
                            max=5, step=0.1, value=0,
                            marks={-5: {'label': '-5'},
                            0: {'label': '0'},
                            5: {'label': '5'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6),
            dbc.Col(children=[
                            'scale',
                            dcc.Slider(id="scale_laplace-slider", min=0, 
                            max=5, step=0.1, value=1,
                            marks={0: {'label': '0'},
                            2.5: {'label': '2.5'},
                            5: {'label': '5'}},
                            tooltip={"placement": "bottom", "always_visible": True},
                            vertical=True)], width=6)
        ])
    ]), 

    html.Div(id='Div_Gaussian_Mixture', children=[
        dcc.Store(id='weights', data=[]),
        dcc.Store(id='means', data=[]),
        dcc.Store(id='stds', data=[]),
        dbc.Row(
            dbc.Col(children=[
                'X',
                dcc.RangeSlider(id="x_gaussian-slider", min=-10, max=10, step=0.1, value=[-1,1],
                marks={-10: {'label': '-10'},
                0: {'label': '0'},
                10: {'label': '10'}},
                tooltip={"placement": "bottom", "always_visible": True})
                ],width={"size": 12}
                )
        ),
        
        dbc.Row([
                dbc.Col(children=[
                                "mean-slider",
                                dcc.Slider(id="mean_gaussian-slider", min=-5, 
                                max=5, step=0.1, value=0,
                                marks={-5: {'label': '-5'},
                                0: {'label': '0'},
                                5: {'label': '5'}},
                                tooltip={"placement": "bottom", "always_visible": True},
                                vertical=True)], width=6),
                dbc.Col(children=[
                                "std-slider",
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
                html.Div('Enter the weight of distribution'),
                dcc.Input(
                id="input",
                type='number')
            ])
        ]),
        dbc.Row([
            dbc.Col(children=[
                html.Button('Add mixture component', id='btn-add', n_clicks=0)
            ]),
            dbc.Col(children=[
                html.Button('Clean', id='btn-clean', n_clicks=0)
            ]),
        ]),
        dbc.Row([
            dbc.Col(children=[
            html.Div('Gaussian Mixture CDF'), 
            dcc.Loading(dcc.Graph(id='Graph15',figure=fig1), type='cube')]),
            dbc.Col(children=[
            html.Div('Gaussian Mixture PDF'), 
            dcc.Loading(dcc.Graph(id='Graph16',figure=fig2), type='cube')])
        ])
        ])
])

@app.callback(
    Output('Div_Normal', 'hidden'),
    Output('Div_Uniform', 'hidden'),
    Output('Div_Poisson', 'hidden'),
    Output('Div_Weibull', 'hidden'),
    Output('Div_Gamma', 'hidden'),
    Output('Div_Expon', 'hidden'),
    Output('Div_Laplace', 'hidden'),
    Output('Div_Gaussian_Mixture', 'hidden'),
    Input('distribution-dropdown', 'value')
)
def update_output(distribution):
    if distribution == 'Normal':
        boolean1=False
        boolean2=True
        boolean3=True
        boolean4=True
        boolean5=True
        boolean6=True
        boolean7=True
        boolean8=True
    elif distribution=='Uniform': 
        boolean1=True
        boolean2=False
        boolean3=True
        boolean4=True
        boolean5=True
        boolean6=True
        boolean7=True
        boolean8=True
    elif distribution=='Poisson': 
        boolean1=True
        boolean2=True
        boolean3=False
        boolean4=True
        boolean5=True
        boolean6=True
        boolean7=True
        boolean8=True
    elif distribution=='Weibull': 
        boolean1=True
        boolean2=True
        boolean3=True
        boolean4=False
        boolean5=True
        boolean6=True
        boolean7=True
        boolean8=True
    elif distribution=='Gamma': 
        boolean1=True
        boolean2=True
        boolean3=True
        boolean4=True
        boolean5=False
        boolean6=True
        boolean7=True
        boolean8=True
    elif distribution=='Exponential': 
        boolean1=True
        boolean2=True
        boolean3=True
        boolean4=True
        boolean5=True
        boolean6=False
        boolean7=True
        boolean8=True
    elif distribution=='Laplace': 
        boolean1=True
        boolean2=True
        boolean3=True
        boolean4=True
        boolean5=True
        boolean6=True
        boolean7=False
        boolean8=True
    else:
        boolean1=True
        boolean2=True
        boolean3=True
        boolean4=True
        boolean5=True
        boolean6=True
        boolean7=True
        boolean8=False
    return boolean1, boolean2, boolean3, boolean4, boolean5, boolean6, boolean7, boolean8

@app.callback(
    Output("Graph1", "figure"),
    Output("Graph2", "figure"),
    Output("Graph17", "figure"),
    Output("Graph18", "figure"),
    Input("x_normal-slider", "value"),
    Input("mean-slider", "value"),
    Input("std-slider", "value")
)
def update_Normal_Graph(value,param1,param2):
    x = np.linspace(value[0], value[1], 100)
    mean = np.linspace(-5, 5, 101)
    std = np.linspace(0,10,101)
    means_for_df1 = []
    means_for_df2 = []
    stds_for_df3=[]
    stds_for_df4=[]
    xs1 = []
    xs2 = []
    xs3=[]
    xs4=[]
    cdfs1=[]
    pdfs1=[]
    cdfs2=[]
    pdfs2=[]
    for i in range(len(mean)):
        cdf = ss.norm.cdf(x, mean[i], param2)
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            means_for_df1.append(mean[i])

    for i in range(len(mean)):
        pdf = ss.norm.pdf(x, mean[i], param2)
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            means_for_df2.append(mean[i])
    
    d1 = {'x': xs1, 'CDF': cdfs1, 
          'mean': means_for_df1}
    d2 = {'x': xs2, 'PDF': pdfs1, 
          'mean': means_for_df2}
    
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    for i in range(len(std)):
        cdf = ss.norm.cdf(x, param1, std[i])
        for j in range(len(cdf)):
            xs3.append(x[j])
            cdfs2.append(cdf[j])
            stds_for_df3.append(std[i])

    for i in range(len(std)):
        pdf = ss.norm.pdf(x,param1, std[i])
        for j in range(len(pdf)):
            xs4.append(x[j])
            pdfs2.append(pdf[j])
            stds_for_df4.append(std[i])
    
    d3 = {'x': xs3, 'CDF': cdfs2, 
          'std': stds_for_df3}
    d4 = {'x': xs4, 'PDF': pdfs2, 
          'std': stds_for_df4}
    
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    fig1 = px.line(df1, x='x', y='CDF', animation_frame='mean')
    fig2 = px.line(df2, x='x', y='PDF', animation_frame='mean')
    fig3 = px.line(df3, x='x', y='CDF', animation_frame='std')
    fig4 = px.line(df4, x='x', y='PDF', animation_frame='std')
    

    return fig1, fig2, fig3, fig4

@app.callback(
    Output("Graph3", "figure"),
    Output("Graph4", "figure"),
    Input("x_uniform-slider", "value"),
    Input("left_boundary-slider", "value"),
    Input("right_boundary-slider", "value")
)
def update_Uniform_Graph(value,param1,param2):
    x = np.linspace(value[0], value[1], 1000)
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.uniform.cdf(x,param1,param2)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.uniform.pdf(x,param1,param2)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    fig1 = go.Figure()
    fig2 = go.Figure()
    
    fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
    fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

    return fig1, fig2

@app.callback(
    Output("Graph5", "figure"),
    Output("Graph6", "figure"),
    Input("occurrences", "value"),
    Input("lambda-slider", "value")
)
def update_Poisson_Graph(value,param1):
    x = np.linspace(0, value, value+1)
    d1 = {'x': np.linspace(0, value, value+1), 'CDF': ss.poisson.cdf(x,param1,loc=0)}
    d2 = {'x': np.linspace(0, value, value+1), 'PDF': ss.poisson.pmf(x,param1,loc=0)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    fig1 = go.Figure()
    fig2 = go.Figure()
    
    fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines+markers'))
    fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines+markers'))

    return fig1, fig2

@app.callback(
    Output("Graph7", "figure"),
    Output("Graph8", "figure"),
    Input("x_weibull-slider", "value"),
    Input("shape-slider", "value"),
    Input("scale_weibull-slider", "value")
)
def update_Weibull_Graph(value,param1,param3):
    x = np.linspace(value[0], value[1], 1000)
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': 
          ss.weibull_min.cdf(x,param1,loc=0,scale=param3)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': 
          ss.weibull_min.pdf(x,param1,loc=0,scale=param3)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    fig1 = go.Figure()
    fig2 = go.Figure()
    
    fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
    fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

    return fig1, fig2

@app.callback(
    Output("Graph9", "figure"),
    Output("Graph10", "figure"),
    Input("x_gamma-slider", "value"),
    Input("a-slider", "value"),
    Input("tetta-slider", "value")
)

def update_Gamma_Graph(value,param1,param2):
    x = np.linspace(value[0], value[1], 1000)
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': 
          ss.gamma.cdf(x,param1,loc=0,scale=param2)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': 
          ss.gamma.pdf(x,param1,loc=0,scale=param2)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    fig1 = go.Figure()
    fig2 = go.Figure()
    
    fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
    fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

    return fig1, fig2

@app.callback(
    Output("Graph11", "figure"),
    Output("Graph12", "figure"),
    Input("x_expon-slider", "value"),
    Input("scale_expon-slider", "value")
)

def update_Expon_Graph(value,param1):
    x = np.linspace(value[0], value[1], 1000)
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': 
          ss.expon.cdf(x,loc=0,scale=1/param1)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': 
          ss.expon.pdf(x,loc=0,scale=1/param1)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    fig1 = go.Figure()
    fig2 = go.Figure()
    
    fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
    fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

    return fig1, fig2

@app.callback(
    Output("Graph13", "figure"),
    Output("Graph14", "figure"),
    Input("x_laplace-slider", "value"),
    Input("shift-slider", "value"),
    Input("scale_laplace-slider", "value")
)

def update_Laplace_Graph(value,param1,param2):
    x = np.linspace(value[0], value[1], 1000)
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': 
          ss.laplace.cdf(x,param1,param2)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': 
          ss.laplace.pdf(x,param1,param2)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    fig1 = go.Figure()
    fig2 = go.Figure()
    
    fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
    fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

    return fig1, fig2

@app.callback(
    Output("Graph15", "figure"),
    Output("Graph16", "figure"),
    Output("weights","data"),
    Output("means","data"),
    Output("stds","data"),
    Input("btn-add", "n_clicks"),
    Input("btn-clean", "n_clicks"),
    Input("x_gaussian-slider", "value"),
    Input("mean_gaussian-slider", "value"),
    Input("std_gaussian-slider", "value"),
    Input("input", "value"),
    Input("weights","data"),
    Input("means","data"),
    Input("stds","data")
)
def update_Mixture_Graph(btn1,btn2,value,param1,param2,w,weights,means, stds):
    x = np.linspace(value[0], value[1], 1000)
    cdf=0
    pdf=0
    if "btn-add" == ctx.triggered_id:
        weights.append(w)
        means.append(param1)
        stds.append(param2)
        for i in range(len(means)):
            cdf += np.array(weights[i]) * ss.norm.cdf(x,means[i],stds[i])
            pdf += np.array(weights[i]) * ss.norm.pdf(x,means[i],stds[i])
    
        d1 = {'x': x, 'CDF': cdf}
        d2 = {'x': x, 'PDF': pdf}
        df1 = pd.DataFrame(data=d1)
        df2 = pd.DataFrame(data=d2)
        
        fig1 = go.Figure()
        fig2 = go.Figure()
        
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
    if "btn-clean" == ctx.triggered_id:
        weights=[]
        means=[]
        stds=[]
        for i in range(len(means)):
            cdf += np.array(weights[i]) * ss.norm.cdf(x,means[i],stds[i])
            pdf += np.array(weights[i]) * ss.norm.pdf(x,means[i],stds[i])
    
        d1 = {'x': x, 'CDF': cdf}
        d2 = {'x': x, 'PDF': pdf}
        df1 = pd.DataFrame(data=d1)
        df2 = pd.DataFrame(data=d2)
        
        fig1 = go.Figure()
        fig2 = go.Figure()
        
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

    return fig1, fig2, weights, means, stds

if __name__ == '__main__':
    app.run_server(debug=True)
