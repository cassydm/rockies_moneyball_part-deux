import pandas as pd

csv_files_dict={"2013":"Games_2013.csv","2014":"Games_2014.csv","2015":"Games_2015.csv","2016":"Games_2016.csv","2017":"Games_2017.csv","2018":"Games_2018.csv","2019":"Games_2019.csv","2020":"Games_2020.csv","2021":"Games_2021.csv","2022":"Games_2022.csv","2023":"Games_2023.csv","2024":"Games_2024.csv"}

df_list=[]

def make_df_func(yr,path):
    path_first="../Project 2/"
    path_second=path
    full_path=path_first + path_second
    df=pd.read_csv(full_path)
    df.rename(columns={"Unnamed: 4":"H/A"},inplace=True)
    df.drop("Unnamed: 2",axis=1,inplace=True)
    df["H/A"].fillna("H",inplace=True)
    df["Year"]=yr
    df_list.append(df)
    return df
    
for key,value in csv_files_dict.items():
    result=make_df_func(key,value)

mega_df=pd.concat(df_list,ignore_index=True)
