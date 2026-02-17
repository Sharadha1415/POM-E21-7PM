import xlrd


def excel_data(filepath, sheetname):
    workbook = xlrd.open_workbook(filepath)                 ## book object
    worksheet = workbook.sheet_by_name(sheetname)           ## sheet object
    rows = worksheet.get_rows()                             ## generator object
    header = next(rows)

    d = {}
    for ele in rows:
        d[ele[0].value] = ele[1].value

    return d













































































