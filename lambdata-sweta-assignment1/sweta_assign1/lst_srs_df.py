import pandas as pd

def lst_srs_cl(myList,df):
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