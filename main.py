start = int(input(" початок діапазону: "))
end = int(input(" кінець діапазону: "))
sum_of_numbers = 0
count = 0
current_number = start
while current_number <= end:
    sum_of_numbers += current_number
    count += 1
    current_number += 1
average = sum_of_numbers / count
print(f"Сума чисел у діапазоні: {sum_of_numbers}")
print(f"Середня арифметичнe у діапазоні: {average}")