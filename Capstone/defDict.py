#!/usr/bin/env python3

def listEm(myList):
    returnData = []
    for key, item in myList.items():
        print(key, item)
        returnData.append([key, item])

    print("Return Data:")
    print(returnData)

towns = {'035': '119 Galmoy Co. Kilkenny', '036': '128 Gowran Co. Kilkenny', '058': '129 Granard Co. Longford', '089': '121 Garrycastle Co. Offaly', '090': '123 Geashill Co. Offaly', '113': '127 Gorey Co. Wexford', '162': '124 Glanarought Co. Kerry', '176': '126 Glenquin Co. Limerick', '195': '125 Glenahiry Co. Tipperary, Waterford', '200': '122 Gaultiere Co. Waterford', '210': '120 Galway Co. Galway', '227': '118 Gallen Co. Mayo'}

for code, name in towns.items():
    print(f"Code: {code}, Name: {name}")

print(towns)
print(type(towns))

print("Function")
listEm(towns)