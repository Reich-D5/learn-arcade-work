"""for i in range(10):
    for j in range(10):
        print("*", end="  ")
    print()

for i in range(10):
    print("*", end=" ")
print()

for i in range(5):
    print("*", end=" ")
print()

for i in range(20):
    print("*", end=" ")
print()

for i in range(5):
    for j in range(10):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(20):
        print("*", end=" ")
    print()

for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()

for i in range(10):
    for j in range(i+1):
        print(j, end=" ")
    print()

for i in range(10):
    for j in range(10-i):
        print(j, end=" ")
    print()
"""
for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for j in range(10-i):
        print(j, end=" ")
    print()
"""
for i in range(1, 12):
    for j in range(1, 12):
        product = i*j
        if product < 10:
            print(" ", end="")
        if product < 100:
            print(" ", end="")
        print(product, end=" ")
    print()

for i in range(1, 10):
    for j in range(9-i, 0, -1):
        print(" ", end=" ")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(j, 0, -1):
        print(j, end=" ")
    print()"""
