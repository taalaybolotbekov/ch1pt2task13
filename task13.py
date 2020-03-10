def number():
    num = int(input("Введите номер: "))
    return([i**2 for i in range(1,num+1) if i**2 <= num])
print(number())