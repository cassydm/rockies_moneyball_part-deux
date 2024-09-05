import pandas as pd
import re
from datetime import datetime

#Make a List of our CSV files by year
csv_files_dict={"2013":"Games_2013.csv","2014":"Games_2014.csv","2015":"Games_2015.csv","2016":"Games_2016.csv","2017":"Games_2017.csv","2018":"Games_2018.csv","2019":"Games_2019.csv","2020":"Games_2020.csv","2021":"Games_2021.csv","2022":"Games_2022.csv","2023":"Games_2023.csv","2024":"Games_2024.csv"}

#Making a list to hold our dataframes
df_list=[]
#Defining a function to pull the CSV files into data frames and store them in our list
def make_df_func(yr,path):
    """
    Reads a CSV file, processes it by renaming and dropping columns, fills missing values,
    adds a year column, and appends the DataFrame to a list.

    Args:
        yr (int): The year to add to the DataFrame.
        path (str): The path to the CSV file.

    Returns:
        df: The processed DataFrame.
    """
    #Creating the full file path
    path_first="../Project 2/"
    path_second=path
    full_path=path_first + path_second
    #Reaing the CSV
    df=pd.read_csv(full_path)
    #Renaming columns important
    df.rename(columns={"Unnamed: 4":"H/A"},inplace=True)
    df.drop("Unnamed: 2",axis=1,inplace=True)
    df["H/A"]=df["H/A"].fillna("H")
    df["Year"]=yr
    df_list.append(df)
    return df

#Running the above function on all CSV files
for key,value in csv_files_dict.items():
    result=make_df_func(key,value)


# Concatnating everything into one df
mega_df=pd.concat(df_list,ignore_index=True)

mega_df["Full_Date"]=mega_df["Date"]+", "+mega_df["Year"]
# Define the range of years
years = list(range(2013, 2024))

# Function to clean and convert date string to the desired format
def convert_date_format(date_str):
    """
    Converts a date string to the format 'YYYY-MM-DD'.

    Removes any text within parentheses from the input string, attempts to parse the cleaned string
    with different years, and returns the date in 'YYYY-MM-DD' format if successful.
    
    Args:
        date_str (str): The date string to convert.

    Returns:
        str: The date in 'YYYY-MM-DD' format or 'Invalid date format' if parsing fails.
    """
     # Remove any non-date characters from the string
    cleaned_date_str = re.sub(r'\(.*?\)', '', date_str).strip()
    
    
    # Try to parse the date string without the day and add a default day
    try:
        date_obj = datetime.strptime(cleaned_date_str, '%A %b %d, %Y')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        # Try with a default day if the day is missing
        try:
            date_obj = datetime.strptime(cleaned_date_str + ' 1, 2023', '%A %b %d, %Y')  # Default day and year
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            return 'Invalid date format'

# Apply the function to the 'Date' column
mega_df['Formatted_Date'] = mega_df['Full_Date'].apply(convert_date_format)

#Removing invalid dates from the mega_df
mega_df_cleaned = mega_df[mega_df['Formatted_Date'] != 'Invalid date format']
#Creating a list from the df of all dates
date_list=mega_df["Formatted_Date"].tolist()

# Creating a dictionary for other metrics to add to mega_df
col_concat_dict={"COL_atbats":"COL_atbats_column.csv",
                 "COL_BA":"COL_ba_column.csv",
                 "COL_Hits":"COL_hits_column.csv",
                 "COL_HR":"COL_hr_column.csv",
                 "COL_KK":"COL_kk_column.csv",
                 "COL_OBP":"COL_obp_column.csv",
                 "COL_walks":"COL_walks_column.csv"}
#Creating a list to hold dataframes
col_df_list=[]
#Defining a function to create one dataframe from several different csv files.
def make_df_cols(name,path):
    """
    Reads a CSV file into a DataFrame and appends it to the global list col_df_list.

    Args:
        name (str): The name associated with the DataFrame (not used in the function).
        path (str): The filename of the CSV file to read.
    """
    path_first="../Project 2/progress_dataframes/"
    path_second=path
    full_path=path_first + path_second
    df=pd.read_csv(full_path,index_col=0)
    col_df_list.append(df)

#Running the make_df_cols function through the dictionary
for key,value in col_concat_dict.items():
    result=make_df_cols(key,value)
#Joining all of the csv files into one    
metric_df = col_df_list[0].join(col_df_list[1:], how='outer')

#Concatnating the metric_df and the mega_df_cleaned
mega_concat_df1=pd.concat([mega_df_cleaned,metric_df],axis=1)

# Doing the same code but for opponent metrics of the same.

# Creating a dictionary for opponent metrics to add to mega_df
col_concat_opp_dict={"OPP_atbats":"Opp_atbats_column.csv",
                 "OPP_BA":"Opp_ba_column.csv",
                 "OPP_Hits":"Opp_hits_column.csv",
                 "OPP_HR":"OPP_HR_column.csv",
                 "OPP_KK":"OPP_strikeouts_column.csv",
                 "OPP_OBP":"Opp_obp_column.csv",
                 "OPP_walks":"Opp_walks_column.csv"}

#Creating a list to hold opponent dataframes
col_df_opp_list=[]

#Defining a function to create one dataframe from several different csv files.
def make_df_opp_cols(name,path):
    """
    Reads a CSV file into a DataFrame and appends it to the global list col_df_opp_list.

    Args:
        name (str): The name associated with the DataFrame (not used in the function).
        path (str): The filename of the CSV file to read.
    """
    path_first="../Project 2/progress_dataframes_opp/"
    path_second=path
    full_path=path_first + path_second
    df=pd.read_csv(full_path,index_col=0)
    col_df_opp_list.append(df)

#Running the make_df_opp_cols function through the dictionary
for key,value in col_concat_opp_dict.items():
    result=make_df_opp_cols(key,value)
#Joining all of the csv files into one    
metric_opp_df = col_df_opp_list[0].join(col_df_opp_list[1:], how='outer')

#Concatnating the metric_opp_df and the mega_df_cleaned
mega_concat_df=pd.concat([mega_concat_df1,metric_opp_df],axis=1)
mega_concat_df

#Making sure values in the table are usable!

#Updating the wins column to be just W/L
# Replace values in a column
mega_concat_df['W/L'] = mega_concat_df['W/L'].replace('L-wo', 'L')
mega_concat_df['W/L'] = mega_concat_df['W/L'].replace('W-wo', 'L')
mega_concat_df['H/A'] = mega_concat_df['H/A'].replace('@', 'A')

#Getting the metrics for analysis
model_df=mega_concat_df[["Gm#","W/L","D/N","H/A","Opp",
                         "COL_at_bats","COL_ba","COL_hits", "COL_hr","COL_kk","COL_obp","COL_walks",
                         "Opp_at_bats","Opp_ba","Opp_hits","OPP_HR_Column","OPP_kk","Opp_obp","Opp_walks"]]

#Removing rows of games that have not been played yet and putting them into their own df.
unplayed_games=model_df.tail(27)
model_df = model_df.iloc[:-27]