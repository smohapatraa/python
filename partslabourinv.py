import pandas as pd
import numpy as nm
honda = pd.read_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\output.xlsx',0)
hsn = pd.read_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\hsncode.xlsx',0)
honda1 = honda.iloc[:,[3,4,9,13,18,19,23,24,25,26,28,29,32,33]]
honda5 = honda1.replace(nm.nan, '', regex=True)
honda5.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\partslabourinvoice.xlsx')
honda2 = pd.pivot_table(honda5,values =['Taxable Amount','CGST Amount','SGST Amount','IGST Amount','Total Tax','Line Item Invoice Amount'],index =['Invoice Number','Invoice Date'],columns =['CGST Rate', ], aggfunc = nm.sum, margins = [True])
hondaa = pd.merge(honda1, hsn,how = 'inner')
honda3 = pd.pivot_table(hondaa,values =['Taxable Amount','CGST Amount','SGST Amount','IGST Amount','Total Tax','Line Item Invoice Amount'],index =['description'],columns =['CGST Rate', ], aggfunc = nm.sum, margins = [True])
honda1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\partslabourinvoice1.xlsx')
honda2.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\partslabourinvoice2.xlsx')
honda3.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\partslabourinvoice3.xlsx')
hondaa.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\workshop\\partslabourinvoicea.xlsx')
