# 3a
def print_triangle(n):
    if n == 1:
        print(1 * "*")
    else:
        print_triangle(n-1)
        print(n * "*")

# print_triangle(4)

# 3b
def print_opposite_triangle(n):
        if n == 1:
            print(1 * "*")
            print("*")
        else:
            print(n * "*")
            print_opposite_triangle(n-1)
            print(n * "*")

# print_opposite_triangle(4)

# 3c
def print_ruler(n):
    if n == 1:
        print("-")
    else:
        print_ruler(n-1)
        print(n * "-")
        print_ruler(n-1)

# print_ruler(4)
