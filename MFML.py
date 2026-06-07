# Solve:
# x + y = 5
# 2x + y = 8

A = [
    [1, 1, 5],
    [2, 1, 8]
]

print("Initial Matrix:")
for row in A:
    print(row)

print("\n--- Forward Elimination ---")

# Pivot = first element of first row
pivot = A[0][0]

print("Pivot =", pivot)

# Calculate factor
factor = A[1][0] / pivot

print("Factor =", factor)
print("Meaning: Row2 = Row2 - Factor * Row1")

# Update Row2
for k in range(len(A[0])):

    print(f"\nColumn {k}")

    print("Before:", A[1])

    A[1][k] = A[1][k] - factor * A[0][k]

    print("After :", A[1])

print("\nMatrix After Elimination:")
for row in A:
    print(row)

print("\n--- Back Substitution ---")

# Solve y
y = A[1][2] / A[1][1]


print("y =", y)
e=A
# Solve x
x = (A[0][2] - A[0][1] * y) / A[0][0]

print("x =", x)

C= x+y
D=C
print(C)
print("\nFinal Answer")
print("x =", x)
print("y =", y)