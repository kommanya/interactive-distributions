import pandas as pd
import numpy as np
import scipy.stats as ss
import i18n


def uniform_func(value,param1,param2):
    x = np.linspace(value[0], value[1], 1000)
    left_boundary = np.round(np.linspace(-5, 5, 100),1)
    right_boundary = np.round(np.linspace(-5, 5, 100),1)
    left_for_df1 = []
    left_for_df2 = []
    right_for_df3=[]
    right_for_df4=[]
    xs1 = []
    xs2 = []
    xs3=[]
    xs4=[]
    cdfs1=[]
    pdfs1=[]
    cdfs2=[]
    pdfs2=[]
    d1 = {'x': np.linspace(value[0], value[1], 1000), 'CDF': ss.uniform.cdf(x,param1,param2-param1)}
    d2 = {'x': np.linspace(value[0], value[1], 1000), 'PDF': ss.uniform.pdf(x,param1,param2-param1)}
    df1 = pd.DataFrame(data=d1)
    df2 = pd.DataFrame(data=d2)
    for i in range(len(left_boundary)):
        cdf = ss.uniform.cdf(x, left_boundary[i],param2-left_boundary[i])
        for j in range(len(cdf)):
            xs1.append(x[j])
            cdfs1.append(cdf[j])
            left_for_df1.append(left_boundary[i])

    for i in range(len(left_boundary)):
        pdf = ss.uniform.pdf(x, left_boundary[i], param2-left_boundary[i])
        for j in range(len(pdf)):
            xs2.append(x[j])
            pdfs1.append(pdf[j])
            left_for_df2.append(left_boundary[i])
        
    d3 = {'x': xs1, 'CDF': cdfs1, 
        i18n.t("components.left boundary"): left_for_df1}
    d4 = {'x': xs2, 'PDF': pdfs1, 
        i18n.t("components.left boundary"): left_for_df2}
        
    df3 = pd.DataFrame(data=d3)
    df4 = pd.DataFrame(data=d4)

    for i in range(len(right_boundary)):
        cdf = ss.uniform.cdf(x, param1,right_boundary[i]-param1)
        for j in range(len(cdf)):
            xs3.append(x[j])
            cdfs2.append(cdf[j])
            right_for_df3.append(right_boundary[i])

    for i in range(len(right_boundary)):
        pdf = ss.uniform.pdf(x,param1, right_boundary[i]-param1)
        for j in range(len(pdf)):
            xs4.append(x[j])
            pdfs2.append(pdf[j])
            right_for_df4.append(right_boundary[i])
        
    d5 = {'x': xs3, 'CDF': cdfs2, 
        i18n.t("components.right boundary"): right_for_df3}
    d6 = {'x': xs4, 'PDF': pdfs2, 
        i18n.t("components.right boundary"): right_for_df4}
        
    df5 = pd.DataFrame(data=d5)
    df6 = pd.DataFrame(data=d6)

    return df1, df2, df3, df4, df5, df6