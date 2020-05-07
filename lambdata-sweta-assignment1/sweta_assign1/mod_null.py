
import pandas as pd
#from sweta_assign1.mod_null import date_null

def data_null(df):
   print(df.isnull().sum())



if __name__ == "__main__":
   data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
   df=pd.DataFrame(data)

   data_null(df)

