# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 11:05:49 2021

@author: Neil
"""
import pandas as pd
location = 'D:/user/anaconda/envs/資料合併練習/'
df1 = pd.read_csv("close_price.csv" , encoding = "utf-8")
df2 = pd.read_csv("lower_BETA_IFRS_2007-2020v2.csv" , encoding = "utf-8")

df1 = df1.rename({"證券代碼" : "公司"} , axis = 1)
#df2 = df2.rename({"年月" : "年月日"} , axis = 1)
df1[["公司"]] = df1[["公司"]].apply(lambda x : x.str.strip()) #移除前後空格
df2[["公司"]] = df1[["公司"]].apply(lambda x : x.str.strip())

df1_idx = df1[df1['日'] ==17].index
df1 = df1.drop(df1_idx)

df1 = df1.sort_values(by = ['公司','年'],ascending = False)
df2 = df2.sort_values(by = ['公司','年'],ascending = False)
#df1["年月日"]= pd.to_datetime(df1["年月日"], format='%Y/%m/%d', errors='coerce') 
#df2["年月日"]= pd.to_datetime(df1["年月日"], format='%Y/%m/%d', errors='coerce')

#if df["年月日"] == "2021/12/17"
#    df
 
#df_year

df3 = df1.groupby("公司")
df_2007 = df3.get_group(2007)


##note 我想要分離年分 再把年份貼進去 合併成一份資料
