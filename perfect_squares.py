import math

def perfect_squares(n):
    if n>=0:
        sr=int(math.sqrt(n))
        return ((sr*sr)==n)
    return False
n=int(input())
print(perfect_squares(n))