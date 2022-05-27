num = int(input()) # сумма первой и последней цифр равна разности второй и третьей цифр.
a = num//1000
num1 = a//100
num2 = a//10 % 10
num3 = a % 10
b = num % 1000
num4 = b //100
print(num1,num2,num3,num4)
