import json

with open( '3uzdevums.json', 'r') as file:
        dati = json.load(file)


print("Kaka vards: ", dati["cat name"])
print("Suna vards: ", dati["dog name"])
print("Trusa vards:", dati["rabbit name"])
    

