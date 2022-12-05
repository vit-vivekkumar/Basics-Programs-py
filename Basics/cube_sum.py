# Input : n = 5
# Output : 225
# 1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225

def cube(n):
  sum=0
  while n!=0:
    sum=sum+(n*n*n)
    n-=1
  return sum


n=5
print(cube(n))
