N = int(input())

homes = [int(lo) for lo in input().split()]
homes.sort()

print(homes[N//2+N%2-1])
