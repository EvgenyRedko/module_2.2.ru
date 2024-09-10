first = int(input('Введите первое :'))
second = int(input('Введите второе :'))
third = int(input('Введите третье :'))
if first == second == third:
    print(3)
elif first == third or first == second or second == third:
    print(2)
else:
     print(0)
