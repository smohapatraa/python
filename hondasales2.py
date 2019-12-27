import pandas as pd
import numpy as nm
dts = int(input("enter day:"))
honda = pd.read_excel('D:\\SHUVLAXMIMOTORS 2016-2017\\1718\\HONDA SALE DEC 2019.xlsx',6)
sdl = pd.read_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\sd_ledger.xlsx',0)
honda1 = honda.iloc[2:,[0,2,5,6,8,9,10,24]]
honda2 = honda1.loc[honda1['Sales Description'] != 'SHOWROOM']
honda3 = honda2.loc[honda2['Day'] >= dts]
honda4 = honda3.sort_values(by=['Day', 'Sales Description'])
honda5 = pd.merge(sdl,honda4, on ='Sales Description')
honda5.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\hondasales\\sales2.xlsx')
