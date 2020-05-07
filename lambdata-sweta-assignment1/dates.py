def split_dates(df['Date']):
   df['month']=pd.DatetimeIndex(df['Date']).month
   df['year']=pd.DatetimeIndex(df['Date']).year
   df['day']=pd.DatetimeIndex(df['Date']).day

   return df