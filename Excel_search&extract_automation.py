import os
import pandas as pd

input_file_path = "your input folder path/"
pattern = 'pattern to search'
path = 'your output file path'
excel_file_list = os.listdir(input_file_path)
df3 = df = pd.DataFrame()
_columnNumber = 0

appended_data = []

for excel_files in excel_file_list:
    # check for .csv suffix files only
    if excel_files.endswith(".csv"):
        df = pd.read_csv(input_file_path + excel_files)
        df1 = df[(df[df.columns[_columnNumber]].str.contains(pattern, regex=True))]
        df2 = pd.DataFrame([[excel_files]])
        if (df1.empty == False):
            appended_data.append(df2)
            appended_data.append(df1)
appended_data = pd.concat(appended_data)
if os.path.exists(path):
    with pd.ExcelWriter(path, mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
        appended_data.to_excel(writer, sheet_name='your sheet name')
else:
    with pd.ExcelWriter(path) as writer:
        appended_data.to_excel(writer, sheet_name='your sheet name')
