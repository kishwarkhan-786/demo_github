from openpyxl import Workbook
workbook=Workbook()
worksheet=workbook.active
worksheet.title="personal_info"
worksheet['A1']="NAME"
worksheet['B1']="PLACE"
worksheet['C1']="PHONE_NUM"
worksheet['D1']="Email"

data_list=[
    ['kishwar','bahrain','9876543657','kishwar@gamail.com'],
    ['vani','bangaluru','9842435667','vani@gamail.com'],
    ['deep','gujarat','9871234567','deep@gmail.com'],
    ['sonali','maharashtra','9873456778','sonali@gmail.com']
]
for data in data_list:
    worksheet.append(data)
    workbook.save(r"C:\Users\abc\PycharmProjects\selenium_training\files\A13 batch detail.xlsx")


















