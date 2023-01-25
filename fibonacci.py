num = int(input('Enter number : '))

first, second, fib = 0, 1, [0,1]

for i in range(num-2):
    next = first + second
    fib.append(next)
    first = second
    second = next
print(f'{fib}')