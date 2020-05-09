Instructions

Usage
#for mod_null
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df=pd.DataFrame(data)


#for date.py
from .dates import split_dates
ddata={"Date": ["02/15/2019", "02/16/2019", "02/17/2019", "02/18/2019"]}
df = pd.DataFrame(ddata)
print(split_dates(df))

#mod_null
from .mod_null import data_null
data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}
df=pd.DataFrame(data)

data_null(df)