import os
import xlwt

import random as rand

sum = input("Enter sum here:")
count = input("Enter count here:")
avg = int(sum) / int(count)
var = int(avg)*50/100
high = int(avg) + int(var)
low = int(avg) - int(var)
book = xlwt.Workbook(encoding="utf-8")
result = book.add_sheet("result")
for i in range(int(sum)):

    if int(sum)>int(avg):

        a = round((rand.randint(int(low), int(high))),-1)

        sum = int(sum) - int(a)
        
        result.write(i,1,int(a))
        
       

    else:

        result.write(i,1,int(sum))
        break

book.save("trial.xls")
    
                     
    
    
