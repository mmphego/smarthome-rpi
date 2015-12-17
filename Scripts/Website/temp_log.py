import csv

# Temp log path
try:
    path = "../../Logs/Temp_Humid.csv"
    with open(path, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            varHum, varTemp = row
except Exception as errmsg:
    varHum, varTemp = [0, 0]
    #raise RuntimeError('Failed to read file due to {}'.format(errmsg))
