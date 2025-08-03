# 1. Basic Nested Loop
print("1. Basic Nested Loop")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print()

# 2. Rectangle of Stars
print("2. Rectangle of Stars")
rows = 4
cols = 5
for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()
print()

# 3. Right-Angled Triangle
print("3. Right-Angled Triangle")
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# 4. Incremental Number Pattern
print("4. Incremental Number Pattern")
n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print()

# 5. Multiplication Table
print("5. Multiplication Table")
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
print()

# 6. Reverse Triangle Pattern
print("6. Reverse Triangle Pattern")
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# 7. Pyramid Pattern
print("7. Pyramid Pattern")
n = 5
for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()
print()

# 8. Floyd’s Triangle
print("8. Floyd’s Triangle")
n = 5
num = 1
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
