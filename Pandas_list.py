# Import pandas 
import pandas as pd
# Declear the list 
list = [1,4,6,8,5,7]
# apply the pandas as series on the list
Exit_series = pd.Series(list)
# Disply the series 

print(Exit_series)


var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)


x = 0
while (x < 100):
  x+=2
print(x)

a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')




  x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)



for num in range(-2,-5,-1):
    print(num, end=", ")



x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)


print(type(0xFF))
print(type({}) is set)
print(type(range(5)))


print(2 * 3 ** 3 * 4)


x = 100
y = 50
print(x and y)



x = 6
y = 2
print(x ** y)
print(x // y)


a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)