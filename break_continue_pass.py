--------------------------------------------------------------------------------
x = int(input("How many candies do you want"))
i = 1
while i <=x:
    print("Candy")
    i+=1


av=5
x = int(input("How many candies do you want"))
i = 1
while i <=x:
    
    if i>av:
        print("Out Of stock, try next tym ")
        break
    print("Candy")
    i+=1

for i in range(1,100):
    if(i%3 ==0):
        continue
    print(i)


for i in range(1,100):
    if(i%3 ==0 or i%5 == 0):
        continue
    print(i)


for i in range(1,100):
    if i % 2==0:
        pass
    else:
        print(i)
      



# av = 5
#
# x = int(input("How many Candies you want?"))
#
# i = 1
# while i <= x:
#
#     if i>av:
#         print("Out of stock")
#         break
#
#
#     print("Candy")
#     i+=1
#
# print("Bye")


# for i in range(1,101):
#
#     if i%3==0 and i%5==0:
#         continue
#
#     print(i)
#
# print("Bye")


for i in range(1,101):

    if(i%2!=0):
        pass

    else:
        print(i)

print("Bye")



# wrtie a code to print first 50 fibonacci series
a = 1
b = 1
for i in range(50):
  print(a)
  print(b)
  a = a + b
  b = b + a

# write a code to check if a given number is prime or not
x=int(input("Enter a no."))
s=0
i=1
while(i<=x):
    if x%i==0:
        s+=1
    i+=1

if s==2:
    print("Prime number")
else:
    print("Not prime")
