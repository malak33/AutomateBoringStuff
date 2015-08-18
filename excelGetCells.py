#! python3
# excelGetCells.py - example on how to get data/work with data from an excel sheet

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet['A1']
sheet['A1'].value
c = sheet['B1']
c.value
'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
'Cell ' + c.coordinate + ' is ' + c.value
sheet['C1'].value
sheet.get_highest_row()
sheet.get_highest_column()
sheet.cell(row=1, column=2)
sheet.cell(row=1, column=2).value
for i in range(1, 8, 2):
    print(i, sheet.cell(row=i, column=2).value)
