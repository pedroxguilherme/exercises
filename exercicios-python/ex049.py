from time import sleep
n1 = float(input("\033[7mType the number you want know the multiplication table: "))
for c in range(0, 11):
    rsl = n1 * c
    print('\033[33m{} x {} = {} '.format(n1, c, rsl ))
    sleep(0.3)