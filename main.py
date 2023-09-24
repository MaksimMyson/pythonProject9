begin = int(input("Початок:"))
end = int(input("Кінець:"))
while begin <= end:
    begin += 1
    print(begin, end="\t")
    if begin % 3 == 0:
        print(f"| Fizz", end="")
        if begin % 5 == 0:
            print(f"| Buzz", end="")
            if begin % 3 == 0 and  begin % 5 == 0:
                print(f"| Fizz Buzz")
            print()
























