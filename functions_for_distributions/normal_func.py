import pandas as pd
import numpy as np
import scipy.stats as ss
import math
import i18n

def normal_func(value,param1,param2):
    x = np.linspace(value[0], value[1], 1000)
    mean = np.round(np.linspace(-5, 5, 100),1)
    std = np.round(np.linspace(0.1,10,99),1)
    means_for_df3 = []
    means_for_df4 = []
    stds_for_df5=[]
    stds_for_df6=[]
    xs1 = []
    xs2 = []
    xs3=[]
    xs4=[]
    cdfs1=[]
    pdfs1=[]
    cdfs2=[]
    pdfs2=[]
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.norm.cdf(x,param1,math.sqrt(param2))}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.norm.pdf(x,param1,math.sqrt(param2))}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    for i in range(len(mean)):
        cdf = ss.norm.cdf(x, mean[i], math.sqrt(param2))
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            means_for_df3.append(mean[i])

    for i in range(len(mean)):
        pdf = ss.norm.pdf(x, mean[i], math.sqrt(param2))
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            means_for_df4.append(mean[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.mean"): means_for_df3}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.mean"): means_for_df4}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    for i in range(len(std)):
        cdf = ss.norm.cdf(x, param1, math.sqrt(std[i]))
        for j in range(len(cdf)):
            xs3.append(x[j])
            cdfs2.append(cdf[j])
            stds_for_df5.append(std[i])

    for i in range(len(std)):
        pdf = ss.norm.pdf(x,param1, math.sqrt(std[i]))
        for j in range(len(pdf)):
            xs4.append(x[j])
            pdfs2.append(pdf[j])
            stds_for_df6.append(std[i])
        
    d5 = {'x': xs3, 'CDF': cdfs2, 
        i18n.t("components.std"): stds_for_df5}
    d6 = {'x': xs4, 'PDF': pdfs2, 
        i18n.t("components.std"): stds_for_df6}
        
    df5 = pd.DataFrame(data=d5)
    df6 = pd.DataFrame(data=d6)

    return df1, df2, df3, df4, df5, df6