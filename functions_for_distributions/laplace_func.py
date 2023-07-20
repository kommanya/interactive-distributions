import pandas as pd
import numpy as np
import scipy.stats as ss
import i18n

def laplace_func(value,param1,param2):
    x = np.linspace(value[0], value[1], 1000)
    shift = np.round(np.linspace(-5, 5, 100),1)
    scale = np.round(np.linspace(0.1,5,49),1)
    shifts_for_df3 = []
    shifts_for_df4 = []
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
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.laplace.cdf(x,param1,param2)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.laplace.pdf(x,param1,param2)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    for i in range(len(shift)):
        cdf = ss.laplace.cdf(x,shift[i],param2)
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            shifts_for_df3.append(shift[i])

    for i in range(len(shift)):
        pdf =  ss.laplace.pdf(x,shift[i],param2)
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            shifts_for_df4.append(shift[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.shift"): shifts_for_df3}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.shift"): shifts_for_df4}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    for i in range(len(scale)):
        cdf =  ss.laplace.cdf(x,param1,scale[i])
        for j in range(len(cdf)):
            xs3.append(x[j])
            cdfs2.append(cdf[j])
            scales_for_df5.append(scale[i])

    for i in range(len(scale)):
        pdf =  ss.laplace.pdf(x,param1,scale[i])
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