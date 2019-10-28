import pandas as pd
import numpy as nm
print("hello")
honda = pd.read_excel('C:\\Users\\Administrator\\Desktop\\s07\\transit\\output.xlsx',0)
honda1=honda.loc[:,['Frame #','Engine No','Model Name','Color Code','Model Variant','Color','Physical Status','Product Name','Selling Dealer','Plant Code','Transporter Code','Transporter Name','Dealer Code','HMSI Invoice Amount','HMSI Load Reference No','Truck Number','Purchase Order No.','Payment Amount','Dispatch Date','Model Code','Manufacturing Date','SAP Invoice Number', 'HSN Code','Reference Number']]
honda2=honda.loc[:,['SAP Invoice Number','Frame #','Model Name','Color Code','Model Variant','Color','HMSI Invoice Amount','Truck Number','Dispatch Date','SAP Invoice Number','HMSI Load Reference No','SAP Invoice Number','Transporter Name']]
honda1.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\transit\\billing1.xlsx')
honda2.to_excel('C:\\Users\\Administrator\\Desktop\\s07\\transit\\transit.xlsx')
