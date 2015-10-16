import csv

# Temp log path
path = "../../Logs/Temp_Humid.csv"
with open(path, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        varHum, varTemp = row
