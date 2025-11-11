a = int(input("Enter value 1: "))
b = int(input("Enter vlaue 2: "))
c = int(input("Enter vlaue 3: "))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print(f"Average is higher than {a}, {b}, {c}")
elif avg > a and avg > b :
    print(f"Average is higher than {a}, {b}")
elif avg > a and avg > c:
    print(f"Average is higher than {a}, {c}")
elif avg > b and avg > c:
    print(f"Average is higher than {b}, {c}")
elif avg > a:
    print(f"Average is higher than {a}")
elif avg > b:
    print(f"Average is higher than {b}")
elif avg > c:
    print(f"Average is higher than {c}")
else:
    print("Invalid input")