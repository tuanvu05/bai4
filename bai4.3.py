S = input('Nhap chuoi:')
for ch in S:
    if ch not in [' ','\t']:
        print(ch.upper())
