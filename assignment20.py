#Q.1 - Create a dataframe with your name , age , mail id and 
#phone number and add your friends’s information to the same.
import pandas as p
d={
    'Name' :['Navjeet','Rukman'],
    'Age' :[19,19],
    'Mail_id' :['ghotranavjeet592@gmail.com','bhartirana9050@gmail.com'],
    'Phone_number' :[95181245677,5465859896]
}
df=p.DataFrame(d)
print(df)

#ANSWER-      name  age                  mail id  phone number
#0    Ayush   20    www.ayush32@gmail.com    7988390399
#1  Sarthak   21  www.sarthak15@Gmail.com    7876391530

#Q.2 -Import the data and print the following :
#a.) First 5 rows of Dataframe 
#b.) First 10 rows of the Dataframe 
#c.) find basic statistics on the particular dataset. 
#d.) Find the last 5 rows of the dataframe 
#e.) Extract the 2nd column and find basic statistics on it

import pandas as p
import numpy as np
df=p.read_csv("weather.csv")
print("The first five rows of dataframe: ",df.head(5))
print("The first ten rows of dataframe: ",df.head(10))
print("Basic statistics of sheet: ",df.describe())
print("The last five rows of dataframe: ",df.tail(5))
print("The second column of dataframe:",df['Location'].describe())

#ANSWER-
# The first five rows of dataframe:          Date  Location  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  \
# 0  11/1/2007  Canberra      8.0     24.3       0.0          3.4       6.3   
# 1  11/2/2007  Canberra     14.0     26.9       3.6          4.4       9.7   
# 2  11/3/2007  Canberra     13.7     23.4       3.6          5.8       3.3   
# 3  11/4/2007  Canberra     13.3     15.5      39.8          7.2       9.1   
# 4  11/5/2007  Canberra      7.6     16.1       2.8          5.6      10.6   

  # WindGustDir  WindGustSpeed WindDir9am      ...      Humidity3pm  \
# 0          NW           30.0         SW      ...               29   
# 1         ENE           39.0          E      ...               36   
# 2          NW           85.0          N      ...               69   
# 3          NW           54.0        WNW      ...               56   
# 4         SSE           50.0        SSE      ...               49   

   # Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  RainToday  \
# 0       1019.7       1015.0         7         7     14.4     23.6         No   
# 1       1012.4       1008.4         5         3     17.5     25.7        Yes   
# 2       1009.5       1007.2         8         7     15.4     20.2        Yes   
# 3       1005.5       1007.0         2         7     13.5     14.1        Yes   
# 4       1018.3       1018.5         7         7     11.1     15.4        Yes   

   # RISK_MM  RainTomorrow  
# 0      3.6           Yes  
# 1      3.6           Yes  
# 2     39.8           Yes  
# 3      2.8           Yes  
# 4      0.0            No  

# [5 rows x 24 columns]
# The first ten rows of dataframe:           Date  Location  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  \
# 0   11/1/2007  Canberra      8.0     24.3       0.0          3.4       6.3   
# 1   11/2/2007  Canberra     14.0     26.9       3.6          4.4       9.7   
# 2   11/3/2007  Canberra     13.7     23.4       3.6          5.8       3.3   
# 3   11/4/2007  Canberra     13.3     15.5      39.8          7.2       9.1   
# 4   11/5/2007  Canberra      7.6     16.1       2.8          5.6      10.6   
# 5   11/6/2007  Canberra      6.2     16.9       0.0          5.8       8.2   
# 6   11/7/2007  Canberra      6.1     18.2       0.2          4.2       8.4   
# 7   11/8/2007  Canberra      8.3     17.0       0.0          5.6       4.6   
# 8   11/9/2007  Canberra      8.8     19.5       0.0          4.0       4.1   
# 9  11/10/2007  Canberra      8.4     22.8      16.2          5.4       7.7   

  # WindGustDir  WindGustSpeed WindDir9am      ...      Humidity3pm  \
# 0          NW           30.0         SW      ...               29   
# 1         ENE           39.0          E      ...               36   
# 2          NW           85.0          N      ...               69   
# 3          NW           54.0        WNW      ...               56   
# 4         SSE           50.0        SSE      ...               49   
# 5          SE           44.0         SE      ...               57   
# 6          SE           43.0         SE      ...               47   
# 7           E           41.0         SE      ...               57   
# 8           S           48.0          E      ...               48   
# 9           E           31.0          S      ...               32   

   # Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  RainToday  \
# 0       1019.7       1015.0         7         7     14.4     23.6         No   
# 1       1012.4       1008.4         5         3     17.5     25.7        Yes   
# 2       1009.5       1007.2         8         7     15.4     20.2        Yes   
# 3       1005.5       1007.0         2         7     13.5     14.1        Yes   
# 4       1018.3       1018.5         7         7     11.1     15.4        Yes   
# 5       1023.8       1021.7         7         5     10.9     14.8         No   
# 6       1024.6       1022.2         4         6     12.4     17.3         No   
# 7       1026.2       1024.2         6         7     12.1     15.5         No   
# 8       1026.1       1022.7         7         7     14.1     18.9         No   
# 9       1024.1       1020.7         7         1     13.3     21.7        Yes   

   # RISK_MM  RainTomorrow  
# 0      3.6           Yes  
# 1      3.6           Yes  
# 2     39.8           Yes  
# 3      2.8           Yes  
# 4      0.0            No  
# 5      0.2            No  
# 6      0.0            No  
# 7      0.0            No  
# 8     16.2           Yes  
# 9      0.0            No  

# [10 rows x 24 columns]
# Basic statistics of sheet:            MinTemp     MaxTemp    Rainfall  Evaporation    Sunshine  \
# count  366.000000  366.000000  366.000000   366.000000  363.000000   
# mean     7.265574   20.550273    1.428415     4.521858    7.909366   
# std      6.025800    6.690516    4.225800     2.669383    3.481517   
# min     -5.300000    7.600000    0.000000     0.200000    0.000000   
# 25%      2.300000   15.025000    0.000000     2.200000    5.950000   
# 50%      7.450000   19.650000    0.000000     4.200000    8.600000   
# 75%     12.500000   25.500000    0.200000     6.400000   10.500000   
# max     20.900000   35.800000   39.800000    13.800000   13.600000   

       # WindGustSpeed  WindSpeed9am  WindSpeed3pm  Humidity9am  Humidity3pm  \
# count     364.000000    359.000000    366.000000   366.000000   366.000000   
# mean       39.840659      9.651811     17.986339    72.035519    44.519126   
# std        13.059807      7.951929      8.856997    13.137058    16.850947   
# min        13.000000      0.000000      0.000000    36.000000    13.000000   
# 25%        31.000000      6.000000     11.000000    64.000000    32.250000   
# 50%        39.000000      7.000000     17.000000    72.000000    43.000000   
# 75%        46.000000     13.000000     24.000000    81.000000    55.000000   
# max        98.000000     41.000000     52.000000    99.000000    96.000000   

       # Pressure9am  Pressure3pm    Cloud9am    Cloud3pm     Temp9am  \
# count   366.000000   366.000000  366.000000  366.000000  366.000000   
# mean   1019.709016  1016.810383    3.890710    4.024590   12.358470   
# std       6.686212     6.469422    2.956131    2.666268    5.630832   
# min     996.500000   996.800000    0.000000    0.000000    0.100000   
# 25%    1015.350000  1012.800000    1.000000    1.000000    7.625000   
# 50%    1020.150000  1017.400000    3.500000    4.000000   12.550000   
# 75%    1024.475000  1021.475000    7.000000    7.000000   17.000000   
# max    1035.700000  1033.200000    8.000000    8.000000   24.700000   

          # Temp3pm     RISK_MM  
# count  366.000000  366.000000  
# mean    19.230874    1.428415  
# std      6.640346    4.225800  
# min      5.100000    0.000000  
# 25%     14.150000    0.000000  
# 50%     18.550000    0.000000  
# 75%     24.000000    0.200000  
# max     34.500000   39.800000  
# The last five rows of dataframe:             Date  Location  MinTemp  MaxTemp  Rainfall  Evaporation  Sunshine  \
# 361  10/27/2008  Canberra      9.0     30.7       0.0          7.6      12.1   
# 362  10/28/2008  Canberra      7.1     28.4       0.0         11.6      12.7   
# 363  10/29/2008  Canberra     12.5     19.9       0.0          8.4       5.3   
# 364  10/30/2008  Canberra     12.5     26.9       0.0          5.0       7.1   
# 365           N           48.0        NNW      ...               22   
# 363         ESE           43.0        ENE      ...               47   
# 364          NW           46.0        SSW      ...               39   
# 365          NW           78.0         NW      ...               13   

     # Pressure9am  Pressure3pm  Cloud9am  Cloud3pm  Temp9am  Temp3pm  \
# 361       1016.1       1010.8         1         3     20.4     30.0   
# 362       1020.0       1016.9         0         1     17.2     28.2   
# 363       1024.0       1022.8         3         2     14.5     18.3   
# 364       1021.0       1016.2         6         7     15.8     25.9   
# 365       1009.6       1009.2         1         1     23.8     28.6   

     # RainToday  RISK_MM  RainTomorrow  
# 361         No      0.0            No  
# 362         No      0.0            No  
# 363         No      0.0            No  
# 364         No      0.0            No  
# 365         No      0.0            No  

# [5 rows x 24 columns]
# The second column of dataframe: count          366
# unique           1
# top       Canberra
# freq           366
# Name: Location, dtype: object 10/31/2008  Canberra     12.3     30.2       0.0          6.0      12.6   

    # WindGustDir  WindGustSpeed WindDir9am      ...      Humidity3pm  \
# 361         NNW           76.0        SSE      ...               15   
# 362 












































































