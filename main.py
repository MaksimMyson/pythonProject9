n = int(input(" Число для вичисления факториала: "))
factorial = 1
count = 1
while count <= n:
    factorial   *= count
    count += 1
    print(f"Факториал числа {n} равняется {factorial}")
