import xlrd

path = r'C:\Users\abc\PycharmProjects\selenium_training\ddt\register_data.xlsx'


def excel_data(sheetname):
    workbook = xlrd.open_workbook(path)                 ## book object
    worksheet = workbook.sheet_by_name(sheetname)        ## sheet object
    rows = worksheet.get_rows()                         ## generator object
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value

    return d

