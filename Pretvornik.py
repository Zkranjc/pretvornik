# -*- encoding: utf-8 -*-
pozdrav = raw_input("Pozdravljeni Bi rad pretvoril km v milje? (odgovori z da/ne): ").lower()
print(pozdrav)

while pozdrav == "da":
    km = float(raw_input("Vnesi število km, ki jih želiš pretvoriti: "))
    print(km)
    milje = km * 0.62137
    print(milje)
    break

ponovno_vprasaj = raw_input("Želite pretvoriti še enkrat? (da/ne)").lower()
if pozdrav == "ne":
    print("Hvala za sodelovanje!")

elif ponovno_vprasaj == "da":
    km = float(raw_input("Vnesi število km, ki jih želiš pretvoriti: "))
    print(km)
    print(milje)
    print ("Hvala za sodelovanje!")
else:
    print("Hvala za sodelovanje")

if pozdrav == "ne":
    print("Hvala za sodelovanje!")






