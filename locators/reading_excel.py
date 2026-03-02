import xlrd
path=r'C:\Users\abc\PycharmProjects\selenium_training\files\A13 batch detail.xlsx'
workbook=xlrd.open_workbook(path)
worksheet=workbook.sheet_by_name("personal_info")
rows=worksheet.get_rows()
print(rows)
for ele in rows:
    print(ele)