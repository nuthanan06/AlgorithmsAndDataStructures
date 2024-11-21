dict = {"January": 2200, "February": 2350, "March":2600, "April": 2130, "May": 2190}

print("1. ", dict["January"] - dict["February"])
print("2. ", dict["January"] + dict["February"] + dict["March"])

for i in dict: 
    if i == 2000: 
        print(list(dict.values()).index(2000))

dict["June"] = 1980
dict["April"] -= 20

print(dict)
print(dict["April"])

    