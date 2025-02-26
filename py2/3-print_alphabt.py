for ascii in range(97, 123):
    if ascii == 101 or ascii == 113:
        continue
    print(chr(ascii).format(), end='')
