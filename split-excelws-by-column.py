import pandas as pd
import openpyxl
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Create workbook and worksheets
wb = Workbook()
ws = wb.active
ws.title = 'D204'
ws1 = wb.create_sheet('D205')

# Reference master list of students
class_list = r"C:\Data\Simon Fraser University\12. Fall 2020\BUS 251 (TA)\Bus 251 D2 (20-3) Class List.xlsx"

# Check the data
# =============================================================================
# df = pd.read_excel(class_list)
# print(df)
# =============================================================================

# Create new dataframes for each tutorial section
df_204 = df[df['Tutorial'] == 'D204']
df_205 = df[df['Tutorial'] == 'D205']

# Copy dataframe rows into worksheets
for r in dataframe_to_rows(df_204, index=False, header=True):
    ws.append(r)
for r in dataframe_to_rows(df_205, index=False, header=True):
    ws1.append(r)

# Save workbook
wb.save(r"C:\Data\Simon Fraser University\12. Fall 2020\BUS 251 (TA)\Class List D204 D205.xlsx")