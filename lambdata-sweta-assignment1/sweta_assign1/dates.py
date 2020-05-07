

import pandas as pd
from .dates import split_dates



def split_dates(df):
   df['month']=pd.DatetimeIndex(df['Date']).month
   df['year']=pd.DatetimeIndex(df['Date']).year
   df['day']=pd.DatetimeIndex(df['Date']).day
   return df


if __name__ == "__main__":
   # only run the code below IF this script is invoked from the command-line
   # not if it is imported from another script

  ddata={"Date": ["02/15/2019", "02/16/2019", "02/17/2019", "02/18/2019"]}
 
  df = pd.DataFrame(ddata)
  print(split_dates(df))