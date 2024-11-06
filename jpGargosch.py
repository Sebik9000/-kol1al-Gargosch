# 1. Pole co má 5 stringových hodnot
pole = ["jaro", "léto", "podzim", "zima", "obdobi"]
print("Základní pole:", pole)

# 2. Přidání prvku "vítr"
pole.append("vítr")
print("Po přidání 'vítr':", pole)

# 3. Odstranění druhého prvku z pole
pole.remove("léto")
print("Po odstranění druhého prvku:", pole)

# 4. Změnění páté hodnoty v poli na "slunce"
pole[4] = "slunce"
print("Po změnění páté hodnoty na 'slunce':", pole)

# 5. Přidání 2 hodnot do pole
pole.extend(["polévka", "štrůdl"])
print("Po přidání dvou hodnot:", pole)
