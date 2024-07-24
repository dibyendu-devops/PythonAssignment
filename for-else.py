nums = [12, 14, 17, 20, 25]
for num in nums:
    if num % 5 == 0:
        print(num)

It will print 20 and 25

nums = [12, 14, 17, 20, 25]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
it will print the output as 20(1st number which is divisble by 5)


nums = [12, 14, 17, 21, 26]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:
    print("Not found")

it will shows not found once

