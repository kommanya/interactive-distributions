from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import plotly.express as px
import i18n
from divs_for_distributions import (
    normal, 
    uniform, 
    poisson,
    weibull, 
    gamma, 
    exponential, 
    laplace, 
    gaussian_mixture)
from functions_for_distributions.normal_func import normal_func
from functions_for_distributions.uniform_func import uniform_func
from functions_for_distributions.poisson_func import poisson_func
from functions_for_distributions.weibull_func import weibull_func
from functions_for_distributions.gamma_func import gamma_func
from functions_for_distributions.exp_func import exp_func
from functions_for_distributions.laplace_func import laplace_func
from functions_for_distributions.gauss_mixture_func import gauss_mixture_func

def create_layout(app:Dash)-> dbc.Container:
    LOCALE = "ru"

    i18n.set("locale", LOCALE)
    i18n.load_path.append("locale")

    DISTRIBS = {i18n.t("distributions.norm"): 0, i18n.t("distributions.uniform"): 1, 
                i18n.t("distributions.poisson"): 2, i18n.t("distributions.weibull"): 3, 
                i18n.t("distributions.gamma"): 4, i18n.t("distributions.exp"): 5, 
                i18n.t("distributions.laplace"): 6, i18n.t("distributions.gauss mixture"):7}

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
        cnt = len(DISTRIBS.keys())
        res = [True]*cnt
        ind = DISTRIBS.get(distribution)
        res[ind] = False
        return tuple(res)
     
    @app.callback(
        Output("Graph1", "figure"),
        Output("Graph2", "figure"),
        Output("Graph3", "figure"),
        Output("Graph4", "figure"),
        Output("Graph5", "figure"),
        Output("Graph6", "figure"),
        Input("x_normal-slider", "value"),
        Input("mean-slider", "value"),
        Input("std-slider", "value")
    )
    def update_Normal_Graph(value,param1,param2):
        df1, df2, df3, df4, df5, df6 = normal_func(value,param1,param2)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.mean"), range_y=[0,1])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.mean"),range_y=[0,1])
        fig5 = px.line(df5, x='x', y='CDF', animation_frame=i18n.t("components.std"), range_y=[0,1])
        fig6 = px.line(df6, x='x', y='PDF', animation_frame=i18n.t("components.std"), range_y=[0,1])

        return fig1, fig2, fig3, fig4, fig5, fig6

    @app.callback(
        Output("Graph7", "figure"),
        Output("Graph8", "figure"),
        Output("Graph9", "figure"),
        Output("Graph10", "figure"),
        Output("Graph11", "figure"),
        Output("Graph12", "figure"),
        Input("x_uniform-slider", "value"),
        Input("left_boundary-slider", "value"),
        Input("right_boundary-slider", "value")
    )
    def update_Uniform_Graph(value,param1,param2):
        df1, df2, df3, df4, df5, df6 = uniform_func(value,param1,param2)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.left boundary"), range_y=[0,1])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.left boundary"),range_y=[0,1])
        fig5 = px.line(df5, x='x', y='CDF', animation_frame=i18n.t("components.right boundary"), range_y=[0,1])
        fig6 = px.line(df6, x='x', y='PDF', animation_frame=i18n.t("components.right boundary"), range_y=[0,1])

        return fig1, fig2, fig3, fig4, fig5, fig6

    @app.callback(
        Output("Graph13", "figure"),
        Output("Graph14", "figure"),
        Output("Graph15", "figure"),
        Output("Graph16", "figure"),
        Input("occurrences", "value"),
        Input("lambda-slider", "value")
    )
    def update_Poisson_Graph(value,param1):
        df1, df2, df3, df4 = poisson_func(value,param1)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.lambda"), range_y=[0,1])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.lambda"), range_y=[0,1])

        return fig1, fig2, fig3, fig4

    @app.callback(
        Output("Graph17", "figure"),
        Output("Graph18", "figure"),
        Output("Graph19", "figure"),
        Output("Graph20", "figure"),
        Output("Graph21", "figure"),
        Output("Graph22", "figure"),
        Input("x_weibull-slider", "value"),
        Input("shape-slider", "value"),
        Input("scale_weibull-slider", "value")
    )
    def update_Weibull_Graph(value,param1,param2):
        df1, df2, df3, df4, df5, df6 = weibull_func(value,param1,param2)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.shape"), range_y=[0,2])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.shape"),range_y=[0,2])
        fig5 = px.line(df5, x='x', y='CDF', animation_frame=i18n.t("components.scale"), range_y=[0,2])
        fig6 = px.line(df6, x='x', y='PDF', animation_frame=i18n.t("components.scale"), range_y=[0,2])

        return fig1, fig2, fig3, fig4, fig5, fig6

    @app.callback(
        Output("Graph23", "figure"),
        Output("Graph24", "figure"),
        Output("Graph25", "figure"),
        Output("Graph26", "figure"),
        Output("Graph27", "figure"),
        Output("Graph28", "figure"),
        Input("x_gamma-slider", "value"),
        Input("a-slider", "value"),
        Input("tetta-slider", "value")
    )

    def update_Gamma_Graph(value,param1,param2):
        df1, df2, df3, df4, df5, df6 = gamma_func(value,param1,param2)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.k"), range_y=[0,1])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.k"),range_y=[0,1])
        fig5 = px.line(df5, x='x', y='CDF', animation_frame=i18n.t("components.tetta"), range_y=[0,1])
        fig6 = px.line(df6, x='x', y='PDF', animation_frame=i18n.t("components.tetta"), range_y=[0,1])

        return fig1, fig2, fig3, fig4, fig5, fig6

    @app.callback(
        Output("Graph29", "figure"),
        Output("Graph30", "figure"),
        Output("Graph31", "figure"),
        Output("Graph32", "figure"),
        Input("x_expon-slider", "value"),
        Input("scale_expon-slider", "value")
    )

    def update_Expon_Graph(value,param1):
        df1, df2, df3, df4 = exp_func(value,param1)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.scale"), range_y=[0,2])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.scale"), range_y=[0,2])

        return fig1, fig2, fig3, fig4

    @app.callback(
        Output("Graph33", "figure"),
        Output("Graph34", "figure"),
        Output("Graph35", "figure"),
        Output("Graph36", "figure"),
        Output("Graph37", "figure"),
        Output("Graph38", "figure"),
        Input("x_laplace-slider", "value"),
        Input("shift-slider", "value"),
        Input("scale_laplace-slider", "value")
    )

    def update_Laplace_Graph(value,param1,param2):
        df1, df2, df3, df4, df5, df6 = laplace_func(value,param1,param2)
        fig1 = go.Figure()
        fig2 = go.Figure()
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))
        fig3 = px.line(df3, x='x', y='CDF', animation_frame=i18n.t("components.shift"), range_y=[0,1])
        fig4 = px.line(df4, x='x', y='PDF', animation_frame=i18n.t("components.shift"),range_y=[0,1])
        fig5 = px.line(df5, x='x', y='CDF', animation_frame=i18n.t("components.scale"), range_y=[0,1])
        fig6 = px.line(df6, x='x', y='PDF', animation_frame=i18n.t("components.scale"), range_y=[0,1])

        return fig1, fig2, fig3, fig4, fig5, fig6

    @app.callback(
        Output("Graph39", "figure"),
        Output("Graph40", "figure"),
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
    def update_Mixture_Graph(btn1,btn2,value,param1,param2,w,weights,means,stds):
        df1, df2 = gauss_mixture_func(btn1,btn2,value,param1,param2,w,weights,means,stds)
        
        fig1 = go.Figure()
        fig2 = go.Figure()
        
        fig1.add_trace(go.Scatter(x=df1['x'], y=df1['CDF'], mode='lines'))
        fig2.add_trace(go.Scatter(x=df2['x'], y=df2['PDF'], mode='lines'))

        return fig1, fig2, weights, means, stds
    
    return dbc.Container([html.Div([
        html.Header(i18n.t("labels.title")),
        dcc.Dropdown([i18n.t("distributions.norm"), i18n.t("distributions.uniform"), 
            i18n.t("distributions.poisson"), i18n.t("distributions.weibull"), 
            i18n.t("distributions.gamma"), i18n.t("distributions.exp"), 
            i18n.t("distributions.laplace"), i18n.t("distributions.gauss mixture")], 
                 id='distribution-dropdown', placeholder="Select a distribution",value=i18n.t("distributions.norm")),
        normal.render(app),
        uniform.render(app),
        poisson.render(app),
        weibull.render(app),
        gamma.render(app),
        exponential.render(app),
        laplace.render(app),
        gaussian_mixture.render(app)
        ])
    ])