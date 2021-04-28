import pandas as pd  
import persian

data = pd.read_csv('500000FamilySample-990402.csv', encoding="utf-8")  

data["SenfName"].fillna("ثبت نشده", inplace = True)

# PreProcessing
for index, row in data.iterrows():
    persian.convert_ar_characters(row['ProvinceName'])
    persian.convert_ar_characters(row['CountyName'])
    persian.convert_ar_characters(row['SenfName'])

for i, row in data.iterrows():
    ifor_val = persian.convert_ar_characters(row['SenfName'])
    data.at[i,'SenfName'] = ifor_val

data.to_csv (r'PreProcessedData.csv', encoding='utf-8-sig')


# Part 1 #
data['BirthDate']= pd.to_datetime(data['BirthDate'],format='%Y-%m-%d')
data1 = data[data["IsTamin_Karfarma"] == 1]
data1 = data1.groupby(['CountyName', data['BirthDate'].dt.year]).Tamin_KargarCount.mean()
data1.to_csv (r'21.csv', encoding='utf-8-sig')


# Part 2 #
data2 = data.groupby(['CountyName', 'IsTamin_Karfarma']).IsBehzisti_Malool.count()
data2.to_csv (r'22.csv', encoding='utf-8-sig')

# Part 3 #
data3 = data.groupby(['ProvinceName', 'Gender']).Cars_Count.count()
data3.to_csv (r'23.csv', encoding='utf-8-sig')


# Part 4 #
data4 = data[data["IsBimarkhas"] == 1]
data4 = data4[data4["SenfName"] != "ثبت نشده"]
data4 = data4.groupby('CountyName').size()
data4.to_csv (r'24.csv', encoding='utf-8-sig')

# Part 5 #
data5 = data.groupby('Cars_Count')[['Trip_AirNonPilgrimageCount_95','Trip_AirNonPilgrimageCount_96','Trip_AirNonPilgrimageCount_97','Trip_AirNonPilgrimageCount_98']].sum()
data5.to_csv(r'25.csv', encoding='utf-8-sig')