#! python3
# - excelWorkbook.py - an example on how to create an excel sheet, and enter information into it. This is using the
# example.xlsx file from the website http://nostarch/automatestuff/

import openpyxl
wb = openpyxl.load_workbook('example.xlsx')
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet3')
sheet
type(sheet)
sheet.title
anotherSheet = wb.get_active_sheet()
anotherSheet