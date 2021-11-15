"""Demonstating some of dictionairies capabilities"""
#declare
schools: dict[str, int]

#initialize
schools = {}

#set key vlaues
schools["UNC"] = 19400
schools["Duke"] = 642
schools["NCSU"] = 1234
print(schools)

# print(schools["UNCC"])
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")