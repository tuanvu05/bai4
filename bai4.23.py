câu = input("Nhập một câu: ")

chữ_cái = 0
chữ_số = 0

for char in câu:
    if char.isalpha():  
        chữ_cái += 1
    elif char.isdigit():  
        chữ_số += 1

print("Số chữ cái:", chữ_cái)
print("Số chữ số:", chữ_số)
