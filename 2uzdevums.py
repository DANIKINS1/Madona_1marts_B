failavards = "pd.txt"
with open(failavards, 'r', encoding="utf-8") as file:
            for line in file:
                rinda = line.strip().split()

                if len(rinda) >= 4:
                    print(rinda[3])  
                else:
                    print("Linijai nav pietiekami daudz kolonnas")
   