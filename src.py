import pandas as pd  

data = pd.read_csv('500000FamilySample-990402.csv', encoding="utf-8")  

# Part 1 #
data1 = data.groupby('CountyName').Daramad_Total_Rials.mean()
data1.to_csv (r'1.csv', encoding='utf-8-sig')


# Part 2 #
data2 = data[data["IsBimarkhas"] == 1]
data2 = data2[data2["ProvinceName"] == "تهران"]
data2 = data2.groupby(['CountyName', 'IsBehzisti_Malool']).IsBimarkhas.count()
data2.to_csv (r'2.csv', encoding='utf-8-sig')

# Part 3 #
data['BirthDate']= pd.to_datetime(data['BirthDate'],format='%Y-%m-%d')
data3 = data[data["IsUrban"] == 1]
data3 = data3[data3["ProvinceName"] == "مازندران"]
data3 = data3.groupby(['CountyName', data['BirthDate'].dt.year]).SenfName.count()
data3.to_csv (r'3.csv', encoding='utf-8-sig')


# Part 4 #
data4 = data.groupby(['ProvinceName','Gender','IsUrban'])[['Variz95','Variz96','Variz97']].sum()
data4.to_csv(r'4.csv', encoding='utf-8-sig')

# Part 5 #
data6 = data.groupby(['CountyName', 'ParentId'], as_index=False).CarPrice_Sum.sum()
data7 = data.groupby(['CountyName', 'ParentId'], as_index=False).size()

merged_left = pd.merge(left=data6, right=data7, how='left', left_on='ParentId', right_on='ParentId')
data6 = merged_left.groupby(['CountyName_x', 'size'], as_index=False).CarPrice_Sum.mean()
data6.to_csv (r'5.csv', encoding='utf-8-sig')