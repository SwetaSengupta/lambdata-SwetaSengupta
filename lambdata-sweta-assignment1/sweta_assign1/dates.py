import pandas as pd


def split_dates(df,col):
            '''returns 3 new columns with month, date, year with a datefield input
              where X is a pandas dataframe and col is a date column'''
             
            df['month']= pd.DatetimeIndex(df[col]).month
            df['year']= pd.DatetimeIndex(df[col]).year
            df['day']= pd.DatetimeIndex(df[col]).day
            return df

    
if __name__ == "__main__":
             # only run the code below IF this script is invoked from 
             # the command-line
             # not if it is imported from another script

             ddata={"Date": ["02/15/2019", "02/16/2019", "02/17/2019", "02/18/2019"],"column2":["hey","hello","hi","namaste"]}
 
             df = pd.DataFrame(ddata)
             print(split_dates(df,'Date'))
