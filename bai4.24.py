câu = input("Nhập một câu: ")

số_chữ_in_hoa = 0
số_chữ_thường = 0

for char in câu:
    if char.isupper():  
       số_chữ_in_hoa  += 1
    elif char.islower():  
       số_chữ_thường  += 1

print("Số chữ hoa:", số_chữ_in_hoa)
print("Số chữ thường:", số_chữ_thường)

