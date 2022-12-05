''' Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

Examples:

Input : N = 4
Output : 30
12 + 22 + 32 + 42
= 1 + 4 + 9 + 16
= 30 '''

# def squre(n):
#   temp=0
#   sum=0
#   while (n!=temp):
#     temp+=1
#     sum=sum+temp**2
#   return sum

# print(squre(4))

def squre(n):
  temp=()
  lst=[]
  for i in n:
    print(i)
    temp=i*i*i
    lst.append(temp)
  return lst

print(squre([5,3,4]))
    
