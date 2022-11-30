'''
1. The function takes in one argument: num, the number to be factorialized
2. The function then checks if num is equal to 0 or 1.
3. If num is equal to 0 or 1, then the function returns 1.
4. If num is not equal to 0 or 1, then the function returns num multiplied by the factorial of num minus 1.
5. The function then returns the factorial of num.
'''

def factorial(num):
  return 1 if (num==0 or num==1) else num*factorial(num-1)

n=5
print(f'factorial of {n} is : {factorial(n)}')

#using lambda function
factorial = lambda x : 1 if (x==1 or x==0) else x*factorial(x-1)

print(f'factorial is :{factorial(5)}')


#Iterative approach

def factorial(num):
  fact=1
  if num==0 or num==1:
    fact=1
  else:
    while(num!=1):
      fact*=num
      num-=1
    return fact
#main code
print(factorial(5))
