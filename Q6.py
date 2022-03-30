num = int(input("Enter int: "))

def recursive(n):
    if n > 0:
        n += recursive(n - 1)
    return n

print(recursive(num))