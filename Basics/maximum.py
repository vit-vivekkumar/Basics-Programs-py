x,y=3,4
print(x if x>y else y)

'''using lambda funtion'''

max = lambda x,y: x if x>y else y

print(max(30,5))


'''
1. The function takes in two arguments: x and y
2. The function then checks if x is greater than y.
3. If x is greater than y, then the function returns x.
4. If x is not greater than y, then the function returns y.
5. The function then returns the maximum of x and y.
'''