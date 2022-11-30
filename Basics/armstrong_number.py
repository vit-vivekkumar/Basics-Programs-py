# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153
 
def armstrong(num):
  n=len(str(num))
  num2=0
  while(num!=0):
    temp = num%10
    num2= num2 + temp**n
    num=num//10
  return num2


num=153
print('armstrong' if num == armstrong(num) else 'not armstrong')