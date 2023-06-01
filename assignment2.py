list = [ 2,3,4,55,56,78,75,69,66,101,100 ]
even_count, odd_count = 0, 0
for num in list:
   #even numbers
   if num % 2 == 0:
      even_count += 1
   #odd numbers
   else:
      odd_count += 1
print("Even numbers available in the list: ", even_count)
print("Odd numbers available in the list: ", odd_count)
