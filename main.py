begin = int(input("Початок:"))
end = int(input("Кінець:"))
while begin <= end:
begin += 1
print(begin, end="\t")
if begin % 7 == 0:
print(f"| % 7", end="")
if begin % 5 == 0:
print(f"| % 5", end="")
print()


















