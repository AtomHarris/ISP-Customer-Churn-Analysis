import os
import pandas as pd

class DataLoader:
    def __init__(self):      
        pass

    def read_data(self, file_path):
        _, file_ext = os.path.splitext(file_path)
        """
        Load data from a CSV, TSV, JSON or Excel file
        """
        if file_ext == '.csv':
            return pd.read_csv(file_path, index_col=None)
        
        elif file_ext == '.tsv':
            return pd.read_csv(file_path, sep='\t')

        elif file_ext == '.json':
            return pd.read_json(file_path)

        elif file_ext in ['.xls', '.xlsx']:
            return pd.read_excel(file_path)

        else:
            raise ValueError(f"Unsupported file format:")
            
class DataFrameMerger:
    def __init__(self):
        pass
    
    def merge_dataframes(self, df1, df2, on, how='inner'):
        """
        Merge two dataframes on specified columns with the specified method.
        """
        merged_df = pd.merge(df1, df2, on=on, how=how)
        return merged_df.sort_values(by=merged_df.columns.tolist())
    
class DataInfo:
    
    def __init__(self,df):
        self.df = df

    def info(self): 
        """
        Displaying Relevant Information on the the Dataset Provided
        """    
        # Counting no of rows 
        print(f'\nTotal Rows : {self.df.shape[0]} \n' + '--'*10 )
      
        # Counting no of columns
        print(f'\nTotal Columns : {self.df.shape[1]} \n' + '--'*10)
        
        # Extracting column names
        column_name =  self.df.columns 
        print(f'\nColumn Names\n' + '--'*10 +  f'\n{column_name} \n \n')
        
        # Data type info
        print(f'Data Summary\n' + '--'*10)
        data_summary = self.df.info() 
        
        # Total null values by each categories
        null_values = self.df.isnull().sum() 
        print(f'\nNull values\n' + '--'*10 + f'\n{null_values} \n \n')

        # Descriptive statistics
        describe =  self.df.describe() 
        print(f'\nDescriptive Statistics\n' + '--'*10 )
        display(describe)
        
        #Display the dataset
        print(f'\nDataset Overview\n'+ '--'*10)
        return self.df.head()