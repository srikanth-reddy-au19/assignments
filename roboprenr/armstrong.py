num = input("Enter a number: ")
len = len(num)  
sum = 0
for i in num:
    sum += pow(int(i),len)
if sum == int(num):
    print(True)    
else:
    print(False)
