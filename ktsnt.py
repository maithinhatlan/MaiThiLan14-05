n = int(input())
def ktsnt(n):
    x = 0
    for i in range(1, n + 1):
        if n % i == 0:
           x = x+1;
    if x == 2:
        return True
    return False
print(ktsnt(n))