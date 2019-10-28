import xlwt
import xlrd
import os

files = os.listdir('C:\\Users\\Administrator\\Desktop\\s07\\s07file')

for i in range(len(files)):
  filename = files[i]
  book = xlwt.Workbook()
  ws = book.add_sheet('s07')  # Add a sheet
  
  f = open(('C:\\Users\\Administrator\\Desktop\\s07\\s07file\\'+filename), 'r+')

  data = f.readlines() # read all lines at once
  for i in range(len(data)):
    row = data[i].split()  # This will return a line of string data, you may need to convert to other formats depending on your use case

    for j in range(len(row)):
      if j == 0:
        s = row[j]
        a = (s[:2]+'-'+s[2:4]+'-'+s[4:8])
        ws.write(i, 1, a)  # Write to cell i, j
      elif j == 1:
        s = row[j]
        a = s[8:]
        ws.write(i, 0, a)  # Write to cell i, j
      elif j == 2:
        s = row[j]
        a = s[14:]
        ws.write(i, j, a)  # Write to cell i, j
      elif j == 3:
        a = row[j]
        ws.write(i, 4, a)  # Write to cell i, j
      elif j == 4:
        a = row[j]
        ws.write(i, 5, a)  # Write to cell i, j
      elif j == 15:
        s = row[j]
        a = float(s[:-1])
        ws.write(i, 6, a)  # Write to cell i, j
      
      elif j == 19:
        s = row[j]
        a = int(s[:-1])
        ws.write(i, 7, a)  # Write to cell i, j
      


      else:
        continue
      

  book.save('C:\\Users\\Administrator\\Desktop\\s07\\s07\\'+ filename + '.xls')
  f.close


