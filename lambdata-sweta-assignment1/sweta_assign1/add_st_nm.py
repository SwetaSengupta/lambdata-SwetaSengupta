from pandas import DataFrame

def add_state_names(my_df):
                """
                 Adds a column of state names to accompany a corresponding column of state abbreviation.

                Params: 
                my_df(pandas.DataFrame) has a column called "abbrev" with state abbreviations.

                Returns:
                copy of the original dataframe, with another column

                """
                new_df = my_df.copy()    
                names_map = {"CA": "CALI", "CO": "COLO", "CT": "CONN"}   
                new_df['name'] = new_df['abbrev'].map(names_map)
                return new_df

if __name__ == "__main__":

                 df = DataFrame({"abbrev":["CA","CO","CT"]})
                 print(df.head())

                 df2 = add_state_names(df)
                 print(df2)
