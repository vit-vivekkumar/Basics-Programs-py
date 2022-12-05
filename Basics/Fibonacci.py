def fab(num):
  if num<=0:
    print('Invalid Input')
  elif num==1:
    return 0
  elif num==2:
    return 1
  else:
    return fab(num-1) + fab(num-2)
print(fab(10))

# def Fibonacci(n):
# 	if n<= 0:
# 		print("Incorrect input")
# 	elif n == 1 or n==2:
# 		return num-1
# 	else:
# 		return Fibonacci(n-1)+Fibonacci(n-2)

# print(Fibonacci(10))

