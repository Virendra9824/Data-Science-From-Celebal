print("\n###----USING-CSV-module----###\n")
import csv

with open("weather.csv", "rt", newline='') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)
    for row in csv_reader:
        print(row)




print("\n###----USING-PANDAS----###\n")

import pandas as pd

df = pd.read_csv('weather.csv')
print(df.head())  
