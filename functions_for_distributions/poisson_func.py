import pandas as pd
import numpy as np
import scipy.stats as ss
import i18n

def poisson_func(value,param1):
    x = np.linspace(0,value, value+1)
    lambdas = np.round(np.linspace(0.1, 50, 49),1)
    lambdas_for_df3 = []
    lambdas_for_df4 = []
    xs1 = []
    xs2 = []
    cdfs1=[]
    pdfs1=[]
    d1 = {'x': np.linspace(0,value, value+1), 'CDF': ss.poisson.cdf(x,param1,loc=0)}
    d2 = {'x': np.linspace(0,value, value+1), 'PDF': ss.poisson.pmf(x,param1,loc=0)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    for i in range(len(lambdas)):
        cdf = ss.poisson.cdf(x, lambdas[i])
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            lambdas_for_df3.append(lambdas[i])

    for i in range(len(lambdas)):
        pdf = ss.poisson.pmf(x, lambdas[i])
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            lambdas_for_df4.append(lambdas[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.lambda"): lambdas_for_df3}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.lambda"): lambdas_for_df4}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    return df1, df2, df3, df4
