x = "Euler"
y = "Heun"
z = "Error Absoluto"
print("\n")
for i in range(1):
    for j in range(1):
        print(f'"Euler"  "Heun"  "ErrorAbs"', end='')
    print('')

for i in range(10):
    for j in range(3):
        print(f'({i},{j})', end='  ')
    print('')
