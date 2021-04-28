# DataWarehouse-IranianWelfareData
In this project, I have analyzed a 2% sample of the Iranian welfare data warehouse. 
This project has two parts. Each of them is about creating cubes from this dataset using ```Pandas``` library (providing data analysis tools for the ```Python``` programming language).
Before doing anything, pre-processing is needed to clean data of inconsistent and NULL indexes. After pre-processing, creating cubes starts.

Cubes are described as bellow:
* The average income of people in each city per month
* Number of members with specific diseases in Tehran province by city and welfare status
* Number of trade licenses of urban people in The Mazandaran province by city and year of birth
* Amount of deposits by year, province, gender and urban status
* Average price of cars per family by city and number of family members

You can run the following command to see results:

Second part cubes are as same as first part except that their data is less important than part1 cubes:
* Average number of workers if a person is an employer by city and year of birth
* Number of disabled people registered in the welfare organization by city and employer or not
* Number of vehicles owned by persons by province and gender
* Number of people with specific diseases who have a union license by city
* The total number of non-pilgrim air trips of people by year, and the number of cars owned

By running the code using following command, you can get results of each cube in a separate .csv file:

```
    python part1.py
    python part2.py
```

A very complete **Persian Report** is also included in report.pdf.

