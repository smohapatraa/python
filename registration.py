import pandas as pd
import numpy as nm
honda = pd.read_excel('C:\\Users\\Administrator\\Desktop\\s07\\registration\\MISfy12019-2020.xlsx',6)
honda1 = pd.read_excel('C:\\Users\\Administrator\\Desktop\\s07\\registration\\MISfy12019-2020.xlsx',7)
honda2=honda.loc[:,['Chasis No','Cust Name','Date','Tax Amt','Ins Amt','Policy #','POLICY DATE','Insurance co','Finance','fees and taxes','Smartchip','smartchip date']]
honda3=honda1.loc[:,['Chasis No','Sales Date','Sales Description','Registration','Insurance','HYP','Finance']]
hondaa = honda2.merge(honda3,on='Chasis No')
hondaa.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\registration\\reginsdetails.xlsx')