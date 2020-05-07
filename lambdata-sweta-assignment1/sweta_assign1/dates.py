

import pandas as pd
from .dates import split_dates

def split_dates(df):
   df['month']=pd.DatetimeIndex(df['Date']).month
   df['year']=pd.DatetimeIndex(df['Date']).year
   df['day']=pd.DatetimeIndex(df['Date']).day

   return df