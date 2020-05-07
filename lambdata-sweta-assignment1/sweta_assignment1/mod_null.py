import pandas
def data_null(df):
   print(df.isnull().sum())
df=pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})