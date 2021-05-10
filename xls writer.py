import glob
import numpy as np
import xlsxwriter
a=glob.glob("path/*.jpg")
#print(a)
b=np.asarray(a)
y=[]
for o in b:
    q=o.split(r"MAGLIE")
    a=q[1]
    o=a[1:]
    y.append(o)
    #print(a[1:])
print(y)
file = open('maglieA.xlsx', 'w+')
workbook = xlsxwriter.Workbook('path/.xlsx')
worksheet = workbook.add_worksheet()
row=1
column = 0
worksheet.write(0, 0, "id")
for item in y :
    worksheet.write(row, column, item)
    row += 1
workbook.close()