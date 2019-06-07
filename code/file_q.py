import sys
import xlrd
import xlwt
split_num = 1000;
print(sys.argv[1])
data = xlrd.open_workbook(sys.argv[1])
print(data)
sheet0 = data.sheet_by_index(0)
sheet_name = data.sheet_names()[0]

print(sheet_name)

rows = sheet0.nrows  # 行总数
print(rows)
cols = sheet0.ncols  # 列总数
print(cols)

title_name = sheet0.row_values(0)
print(title_name)
i = 1
while (i < rows):
    wb = xlwt.Workbook(encoding='utf-8', style_compression=0);
    ws = wb.add_sheet('sheet1', cell_overwrite_ok=True)
    k = 0
    for data in title_name:
        ws.write(0, k, data)
        k = k + 1
    j = 1
    while (j < split_num):
        row_data = sheet0.row_values(i)
        k = 0
        for data in row_data:
            ws.write(j, k, str(data))
            k = k + 1
        j = j + 1
        i = i + 1
        if (i == rows):
            break
    save_name = './' + str(i) + 'test.xls'
    wb.save(save_name)