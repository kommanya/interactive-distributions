import pandas as pd
import numpy as np
import scipy.stats as ss
import i18n

def gamma_func(value,param1, param2):
    x = np.linspace(value[0], value[1], 1000)
    k = np.round(np.linspace(0.1, 10,99),1)
    tetta = np.round(np.linspace(0.1, 10, 99),1)
    k_for_df3 = []
    k_for_df4 = []
    tettas_for_df5=[]
    tettas_for_df6=[]
    xs1 = []
    xs2 = []
    xs3=[]
    xs4=[]
    cdfs1=[]
    pdfs1=[]
    cdfs2=[]
    pdfs2=[]
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.gamma.cdf(x, param1,loc=0, scale=param2)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.gamma.cdf(x, param1,loc=0, scale=param2)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    for i in range(len(k)):
        cdf = ss.gamma.cdf(x, k[i],loc=0, scale=param2)
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            k_for_df3.append(k[i])

    for i in range(len(k)):
        pdf = ss.gamma.pdf(x, k[i],loc=0, scale=param2)
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            k_for_df4.append(k[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.k"): k_for_df3}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.k"): k_for_df4}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    for i in range(len(tetta)):
        cdf = ss.gamma.cdf(x, param1, loc=0, scale=tetta[i])
        for j in range(len(cdf)):
            xs3.append(x[j])
            cdfs2.append(cdf[j])
            tettas_for_df5.append(tetta[i])

    for i in range(len(tetta)):
        pdf = ss.gamma.pdf(x, param1, loc=0, scale=tetta[i])
        for j in range(len(pdf)):
            xs4.append(x[j])
            pdfs2.append(pdf[j])
            tettas_for_df6.append(tetta[i])
        
    d5 = {'x': xs3, 'CDF': cdfs2, 
        i18n.t("components.tetta"): tettas_for_df5}
    d6 = {'x': xs4, 'PDF': pdfs2, 
        i18n.t("components.tetta"): tettas_for_df6}
        
    df5 = pd.DataFrame(data=d5)
    df6 = pd.DataFrame(data=d6)

    return df1, df2, df3, df4, df5, df6