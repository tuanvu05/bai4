input_string = input("Nhập chuỗi các số nhị phân: ")
binary_numbers = input_string.split(',')
print("Các giá trị được nhập:")
for binary in binary_numbers:
    print(binary.strip())  
