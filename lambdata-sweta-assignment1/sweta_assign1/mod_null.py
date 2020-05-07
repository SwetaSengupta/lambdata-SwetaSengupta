
import pandas as pd
#from sweta_assign1.mod_null import date_null

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df=pd.DataFrame(data)

def data_null(df):
   print(df.isnull().sum())
