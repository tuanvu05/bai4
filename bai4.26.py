so_du = 0

print("Nhập nhật ký giao dịch (theo định dạng 'D 100' hoặc 'W 50'). Nhập 'thoát' để kết thúc:")

while True:
    giao_dich = input()

    if giao_dich.lower() == 'thoát':
        break

    try:
        loai_giao_dich, so_tien = giao_dich.split()
        so_tien = int(so_tien)

        if loai_giao_dich == 'D':  
            so_du += so_tien
        elif loai_giao_dich == 'W':
            so_du -= so_tien
        else:
            print("Giao dịch không hợp lệ. Vui lòng nhập lại.")

    except ValueError:
        print("Lỗi nhập liệu. Vui lòng nhập theo định dạng 'D 100' hoặc 'W 50'.")

print("Số tiền thực trong tài khoản:", so_du)

