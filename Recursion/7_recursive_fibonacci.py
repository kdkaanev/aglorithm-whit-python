def calc_fibonacci(n):
    if n <= 1:
        return 1
    return  calc_fibonacci(n - 1) + calc_fibonacci(n - 2)



n = int(input())

print(calc_fibonacci(n))
