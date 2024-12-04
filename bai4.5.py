
ds = input('Danh sách: ')
'''Sử dụng hàm split() để chia chuỗi thành danh sách
với các phần tử cách nhau bởi dấu trống hoặc tab'''
elements = ds.split()
print("Dãy theo thứ tự ngược lại là:", ' '.join(elements[::-1]))
