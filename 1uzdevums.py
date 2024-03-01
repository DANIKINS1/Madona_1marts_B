import csv

failavards = "pd.csv"




with open(failavards, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


