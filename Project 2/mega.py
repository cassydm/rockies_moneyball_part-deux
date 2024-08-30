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
    df["H/A"].fillna("H",inplace=True)
    df["Year"]=yr
    df_list.append(df)
    return df

#Running the above function on all CSV files
for key,value in csv_files_dict.items():
    result=make_df_func(key,value)


# Concatnating everything into one df
mega_df=pd.concat(df_list,ignore_index=True)

#Processing the date into somethign usable
mega_df['Full_Date'] = mega_df['Date'] +", "+ mega_df["Year"]
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
    # Remove anything in parentheses and strip leading/trailing spaces
    
    # Try to extract the year if present
    for year in years:
        try:
            # Try to parse with the current year
            date_obj = datetime.strptime(cleaned_date_str + f', {year}', '%A %b %d, %Y')
            return date_obj.strftime('%Y-%m-%d')
        except ValueError:
            # If parsing fails, try the next year
            continue
    
    # If no valid date found, return a placeholder value
    return 'Invalid date format'

# Apply the function to the 'Date' column
mega_df['Formatted_Date'] = mega_df['Full_Date'].apply(convert_date_format)

#Creating a list from the df of all dates
date_list=mega_df["Formatted_Date"].tolist()


mega_df
