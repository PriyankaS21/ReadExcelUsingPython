import pandas as pd

# READ EXCEL USIGN PYTHON PANDAS
dataframe = pd.read_excel(f'DATA\\data.xlsx')
print(dataframe)

# READ SPECIFIC TAB FROM EXCEL FILE USING PYTHON PANDAS
dataframe2 = pd.read_excel(f'DATA\\data.xlsx', sheet_name='Sheet2')
print(dataframe2)


# READ MUTLIPLE TAB OF AN EXCEL FILE AT A TIME. IT WILL RETURN A DICTIOANRY HAVING KEY AS TAB NAME AND VALUE AS DATAFRAME
dataframe3 = pd.read_excel(f'DATA\\data.xlsx', sheet_name=['Sheet1','Sheet2'])
print(dataframe3)

