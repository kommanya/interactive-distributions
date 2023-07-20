import pandas as pd
import numpy as np
import scipy.stats as ss
import i18n

def exp_func(value,param1):
    x = np.linspace(value[0], value[1], 1000)
    scale = np.round(np.linspace(0.1, 5, 49),1)
    scales_for_df3 = []
    scales_for_df4 = []
    xs1 = []
    xs2 = []
    cdfs1=[]
    pdfs1=[]
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.expon.cdf(x,loc=0,scale=1/param1)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.expon.pdf(x,loc=0,scale=1/param1)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    for i in range(len(scale)):
        cdf = ss.expon.cdf(x,loc=0,scale=1/scale[i])
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            scales_for_df3.append(scale[i])

    for i in range(len(scale)):
        pdf = ss.expon.pdf(x,loc=0,scale=1/scale[i])
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            scales_for_df4.append(scale[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.scale"): scales_for_df3}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.scale"): scales_for_df4}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    return df1, df2, df3, df4
