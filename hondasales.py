import pandas as pd
import numpy as nm
dts = int(input("enter day:"))
honda = pd.read_excel('D:\\SHUVLAXMIMOTORS 2016-2017\\1718\\HONDA SALE DEC 2019.xlsx',6)
honda1 = honda.iloc[2:,[0,2,8,9,10,16,41,24,36,45,26,27,28,29,37,42,21,43,44,19,20,22,23,31]]
honda2 = honda1.loc[honda1['Sales Description'] == 'SHOWROOM']
honda3 = honda2.loc[honda2['Day'] >= dts]
honda3.insert(24, "DebitCredit", "D")
honda3.insert(25, "DebitCredit2", "C")
honda3.insert(26, "Cost Category", "")
honda3.insert(27, "Cost Centre", "")
honda3.insert(28, "VchType", "Journal")
honda3.insert(29, "SALES-UNBILLED", "SALES-UNBILLED")
honda3.insert(30, "Vehicle Registration A/c", "Vehicle Registration A/c")
honda3.insert(31, "REGISTRATION2", "REGISTRATION2")
honda3.insert(32, "Vehicle Insurance A/c", "Vehicle Insurance A/c")
honda3.insert(33, "AMC", "AMC")
honda3.insert(34, "TEFFLON COATING", "TEFFLON COATING")
honda3.insert(35, "Accessories", "Accessories")
honda3.insert(36, "Access2", "Accessories2")
honda3.insert(37, "Cash", "Cash")
honda3.insert(38, "CASH DISCOUNT", "CASH DISCOUNT")
honda3.insert(39, "JOYCLUB", "JOYCLUB")
honda3.insert(40, "HYPOTHECATION", "HYPOTHECATION")
honda3.insert(41, "Receipt", "Receipt")
column1 = ['Vch No','Date','Particulars','Amount','DebitCredit','Cost Category','Cost Centre','Narration for Each Entry','Narration','VchType']
honda3.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\sales.xlsx')
exshowroom = honda3.iloc[:,[0,2,6,7,24,26,27,1,1,28]]
exshowroom1 = honda3.iloc[:,[0,2,29,7,25,26,27,1,1,28]]
exshowroom1.columns = column1
exshowroom.columns = column1
reg1 = honda3.iloc[:,[6,2,6,8,24,26,27,1,1,28]]
reg1.columns = column1
reg11 = honda3.iloc[:,[6,2,31,8,25,26,27,1,1,28]]
reg11.columns = column1
reg2 = honda3.iloc[:,[0,2,6,9,24,26,27,1,1,28]]
reg2.columns = column1
reg22 = honda3.iloc[:,[0,2,30,9,25,26,27,1,1,28]]
reg22.columns = column1
ins = honda3.iloc[:,[0,2,6,10,24,26,27,1,1,28]]
ins2 = honda3.iloc[:,[0,2,32,10,25,26,27,1,1,28]]
ins.columns = column1
ins2.columns = column1
hyp = honda3.iloc[:,[0,2,6,11,24,26,27,1,1,28]]
hyp.columns = column1
hyp2 = honda3.iloc[:,[0,2,40,11,25,26,27,1,1,28]]
hyp2.columns = column1
amc = honda3.iloc[:,[6,2,6,12,24,26,27,1,1,28]]
amc.columns = column1
amc2 = honda3.iloc[:,[6,2,33,12,25,26,27,1,1,28]]
amc2.columns = column1
tc = honda3.iloc[:,[6,2,6,13,24,26,27,1,1,28]]
tc.columns = column1
tc2 = honda3.iloc[:,[6,2,34,13,25,26,27,1,1,28]]
tc2.columns = column1
acc1 = honda3.iloc[:,[0,2,6,14,24,26,27,1,1,28]]
acc1.columns = column1
acc11 = honda3.iloc[:,[0,2,35,14,25,26,27,1,1,28]]
acc11.columns = column1
acc2 = honda3.iloc[:,[6,2,6,15,24,26,27,1,1,28]]
acc2.columns = column1
acc22 = honda3.iloc[:,[6,2,36,15,25,26,27,1,1,28]]
acc22.columns = column1
jc = honda3.iloc[:,[0,2,6,16,24,26,27,1,1,28]]
jc.columns = column1
jc1 = honda3.iloc[:,[0,2,39,16,25,26,27,1,1,28]]
jc1.columns = column1
cash1 = honda3.iloc[:,[0,2,6,17,25,26,27,1,1,41]]
cash11 = honda3.iloc[:,[0,2,37,17,24,26,27,1,1,41]]
cash1.columns = column1
cash11.columns = column1
cash2 = honda3.iloc[:,[6,2,6,18,25,26,27,1,1,41]]
cash22 = honda3.iloc[:,[6,2,37,18,24,26,27,1,1,41]]
cash2.columns = column1
cash22.columns = column1
chq = honda3.iloc[:,[0,2,6,19,25,26,27,1,1,28]]
chq.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\94chq.xlsx')
swipe = honda3.iloc[:,[0,2,6,20,25,26,27,1,1,28]]
swipe.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\95swipe.xlsx')
cd = honda3.iloc[:,[0,2,6,21,25,26,27,1,1,28]]
cd1 = honda3.iloc[:,[0,2,38,21,24,26,27,1,1,28]]
cd.columns = column1
cd1.columns = column1
hmsiex = honda3.iloc[:,[0,2,6,22,25,26,27,1,1,28]]
hmsiex.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\97hmsiex.xlsx')
finamt = honda3.iloc[:,[0,2,6,23,25,26,27,1,1,28]]
finamt1 = honda3.iloc[:,[0,2,5,23,24,26,27,1,1,28]]
finamt.columns = column1
finamt1.columns = column1
journal = pd.concat([exshowroom, exshowroom1, reg1, reg11, reg2, reg22, ins, ins2, hyp, hyp2, amc, amc2, tc, tc2, acc1, acc11, acc2, acc22, jc, jc1, cash1, cash11, cash2, cash22, cd, cd1, finamt, finamt1])
journal = journal.loc[journal['Amount'] > 0]
journal.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\journal.xlsx')
exshowroom.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\1exshowroom.xlsx')
exshowroom1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\1exshowroom1.xlsx')
reg1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\2reg1.xlsx')
reg11.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\2reg11.xlsx')
reg2.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\3reg2.xlsx')
reg22.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\3reg22.xlsx')
amc.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\6amc.xlsx')
amc2.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\6amc2.xlsx')
acc1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\8acc1.xlsx')
acc11.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\8acc11.xlsx')
acc2.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\9acc2.xlsx')
acc22.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\9acc22.xlsx')
jc.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\91jc.xlsx')
jc1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\91jc1.xlsx')
cash1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\92cash1.xlsx')
cash11.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\92cash11.xlsx')
cash2.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\93cash2.xlsx')
cash22.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\93cash22.xlsx')
cd.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\96cd.xlsx')
cd1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\96cd1.xlsx')
finamt.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\98finamt.xlsx')
finamt1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\files\\98finamt1.xlsx')

