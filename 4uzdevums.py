import json
import csv

def read_json(file_name):
    try:
        with open(file_name, 'r') as f:
            data = json.load(f)
            print("Datu nolasīti no JSON faila:")
            print(data)
    except FileNotFoundError:
        print("Kļūda: Faila nav atrasts.")
    except json.decoder.JSONDecodeError:
        print("Kļūda: Nevarēja nolasīt JSON failu.")

def read_txt(file_name):
    try:
        with open(file_name, 'r') as f:
            data = f.read()
            print("Datu nolasīti no TXT faila:")
            print(data)
    except FileNotFoundError:
        print("Kļūda: Faila nav atrasts.")

def read_csv(file_name):
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            print("Datu nolasīti no CSV faila:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Kļūda: Faila nav atrasts.")
    except csv.Error:
        print("Kļūda: Nevarēja nolasīt CSV failu.")

def main():
    file_name = input("Ievadiet faila nosaukumu: ")
    file_format = input("Ievadiet faila formātu (json, txt, csv): ")

    if file_format.lower() == 'json':
        read_json(file_name)
    elif file_format.lower() == 'txt':
        read_txt(file_name)
    elif file_format.lower() == 'csv':
        read_csv(file_name)
    else:
        print("Kļūda: Nepareizs faila formāts.")

if __name__ == "__main__":
    main()