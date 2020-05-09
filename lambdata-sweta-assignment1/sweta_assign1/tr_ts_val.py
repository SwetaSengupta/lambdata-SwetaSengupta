import pandas as pd
def train_test_val(df):
                #Train/validate/test split function for a dataframe
                import pandas as pd
                from sklearn.model_selection import train_test_split
                train, test = train_test_split(df, train_size=0.85, test_size=0.15, 
                                  random_state=42)
                train, val = train_test_split(train, train_size=0.85, test_size=0.15, 
                                  random_state=42)
                return train.head(),val.head(),test.head()


if __name__ == "__main__":
             # only run the code below IF this script is invoked from 
             # the command-line
             # not if it is imported from another script                                  

            url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data'
            column_headers=['zero','One','two','three','four','five','six','seven','eight','nine','ten',
                            'eleven','twelve','thirteen','fourteen','fifteen']
                  
            df = pd.read_csv(url,header=None,na_values='?',names=column_headers, skiprows=None)
            print(train_test_val(df))