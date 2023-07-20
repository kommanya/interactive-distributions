import pandas as pd
import numpy as np
import scipy.stats as ss
import i18n

def weibull_func(value,param1, param2):
    x = np.linspace(value[0], value[1], 1000)
    shape = np.round(np.linspace(0.1, 10, 99),1)
    scale = np.round(np.linspace(0.1, 10, 99),1)
    shapes_for_df3 = []
    shapes_for_df4 = []
    scales_for_df5=[]
    scales_for_df6=[]
    xs1 = []
    xs2 = []
    xs3=[]
    xs4=[]
    cdfs1=[]
    pdfs1=[]
    cdfs2=[]
    pdfs2=[]
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.weibull_min.cdf(x, param1,loc=0, scale=param2)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.weibull_min.pdf(x, param1,loc=0, scale=param2)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)

    for i in range(len(shape)):
        cdf = ss.weibull_min.cdf(x, shape[i],loc=0, scale=param2)
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            shapes_for_df3.append(shape[i])

    for i in range(len(shape)):
        pdf = ss.weibull_min.pdf(x, shape[i],loc=0, scale=param2)
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            shapes_for_df4.append(shape[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.shape"): shapes_for_df3}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.shape"): shapes_for_df4}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    for i in range(len(scale)):
        cdf = ss.weibull_min.cdf(x, param1, loc=0, scale=scale[i])
        for j in range(len(cdf)):
            xs3.append(x[j])
            cdfs2.append(cdf[j])
            scales_for_df5.append(scale[i])

    for i in range(len(scale)):
        pdf = ss.weibull_min.pdf(x, param1, loc=0, scale=scale[i])
        for j in range(len(pdf)):
            xs4.append(x[j])
            pdfs2.append(pdf[j])
            scales_for_df6.append(scale[i])
        
    d5 = {'x': xs3, 'CDF': cdfs2, 
        i18n.t("components.scale"): scales_for_df5}
    d6 = {'x': xs4, 'PDF': pdfs2, 
        i18n.t("components.scale"): scales_for_df6}
        
    df5 = pd.DataFrame(data=d5)
    df6 = pd.DataFrame(data=d6)

    return df1, df2, df3, df4, df5, df6