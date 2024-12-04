input_numbers = input("Nhập các số, phân tách bởi dấu cách: ")

numbers = [int(num) for num in input_numbers.split()]

Số_lẻ = [num for num in numbers if num % 2 != 0]

print("Danh sách các số lẻ:", Số_lẻ)
