a = int(input("Початок:"))
b = int(input("Кінець:"))
for num in range(a, b + 1):
    if num % 7 == 0:
        print(num)