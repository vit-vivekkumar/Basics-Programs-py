'''
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.

The idea to solve this problem is to iterate the val from start to end using a for loop and for every number, if it is greater than 1, check if it divides n. If we find any other number which divides, print that value.
'''
# def prime(num):
#   for i in range(2,(num)):
#     return 'prime' if num%i!=0 else 'Not prime'
  
# print(prime(4))

def prime(l1,l2):
  prime_num=[]
  j=1
  for i in range(l1,l2):
    j+=1
    print(j)
    print(i)
    if i%j!=0:
      prime_num.append(i)
  return prime_num

  
#How many prime number in given list
print(prime(4,12))

