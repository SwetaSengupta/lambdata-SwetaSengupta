import unittest
import pandas as pd
from sweta_assign1.dates import split_dates 

class test_dt(unittest.TestCase):    
     def test_col_no(self):

# expect that it has three more column and the same number of rows, after we invoke the function
    # expect that certain column names exist before and certain col names exist after
    #expects certain values in certain columns
             ddata={"Date": ["02/15/2019", "02/16/2019", "02/17/2019", "02/18/2019"],"column2":["hey","hello","hi","namaste"]} 
             df = pd.DataFrame(ddata)
    
    

             self.assertEqual(list(df.columns),['Date','column2'])
             result = split_dates(df,'Date')
             self.assertEqual(list(result.columns),['Date','column2','month','year','day'])
             self.assertEqual(result.iloc[0]["Date"] , "02/15/2019")
             self.assertEqual( result.iloc[0]["month"], 2)
             self.assertEqual(result.iloc[0]["year"], 2019)
             self.assertEqual(result.iloc[0]["day"] , 15)

if __name__=="__main__":
    unittest.main()
        