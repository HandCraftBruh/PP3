def fact(x, n):
    def fac(n):
        if n < 1:
            return 1
        else:
            return n*fac(n-1)
    return x**n/fac(n)
print(fact(5, 2))


def func():
    s = [int(i) for i in input('Введите последовательность:').split() if int(i)]
    print(*s[::2])
func()