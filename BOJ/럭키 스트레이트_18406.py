N = str(input())

halfN = len(N)//2
head, tail = N[:halfN], N[halfN:]
is_lucky = sum(map(int, head)) == sum(map(int, tail))
print('LUCKY' if is_lucky else 'READY')
