from dash import ctx
import pandas as pd
import numpy as np
import scipy.stats as ss


def gauss_mixture_func(btn1,btn2,value,param1,param2,w,weights,means,stds):
    x = np.linspace(value[0], value[1], 1000)
    cdf=0
    pdf=0
    if "btn-add" == ctx.triggered_id:
        weights.append(w)
        means.append(param1)
        stds.append(param2)
    
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
    return df1, df2
