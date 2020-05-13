import pandas as pd

def lst_srs_cl(myList,df):

     """Single function to take a list, turn it into a series and add it to a dataframe as a new column.
        Params: 
                myList is a single list
                df is a dataframe which contains a few columns
        Returns:
                copy of the original dataframe, with an added column which has all the values from myList

     """
     mySeries = pd.Series(myList)      
     df.insert(0,"Gender", mySeries)
     return df

if __name__ == "__main__":
             # only run the code below IF this script is invoked from 
             # the command-line
             # not if it is imported from another script

            myList = ['boy','boy','boy','boy','girl']                                                                                                                
            mySeries = pd.Series(myList)                                                                                                                             

            data = {'Name':['Tom', 'Nick', 'Krish', 'Jack','Jenny'],
                   'Age':[20, 21, 19, 18,21]}
            df=pd.DataFrame(data)
            print(lst_srs_cl(myList,df))