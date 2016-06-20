import xlrd
import xlwt


def open_excel(file_name = 'words.xls'):
    try:
        data = xlrd.open_workbook(file_name)
        return data
    except Exception as e:
        print(e)


def deal_string(s):
    s = s.strip()
    if len(s) > 0:
        index = s.index('.')
        if index > 0:
            s = s[index+1:]
    return s.strip()


def write_one_to_sheet(sheet, row, col, value):
    """
    write one data to excel sheet
    :param sheet: worksheet object
    :param row:
    :param col:
    :param value:
    :return:
    """
    ctype = 1
    if sheet is None:
        return
    print('row', row)
    print('col', col)
    print('value', value)
    sheet.write(row, col, value)


def trans(lists, sheet, count):
    if lists is None and sheet is None:
        return
    row = 0
    col = 0
    num = 0
    for item in lists:
        index = item.index(' ')

        if index > 0:
            word = item[0: index]
            meaning = item[index+1:]
            write_one_to_sheet(sheet, row, col, word)
            col = col + 1
            write_one_to_sheet(sheet, row, col, meaning)
            col = col + 1
            num = num + 1
            if col > count - 1:
                col = 0
                row = row + 1
    return num


file = open('words.txt', 'r')
line = deal_string(file.readline())
word_list = []
while len(line) > 0:
    print(line)
    line = deal_string(file.readline())
    if len(line) > 0:
        word_list.append(line)
word_list.sort()
print(word_list)
excel = open_excel()
table = excel.sheet_by_index(0)
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('words')
trans(word_list, worksheet, 6)
print(len(word_list))
workbook.save('words.xls')
