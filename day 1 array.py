arr = [10,20,30,40]

#indexing:
print(arr[0])
#output - 10

#traversal(visiting each & every element):
for num in arr :
    print(num)
#output - 10 20 30 40

#sum of array :
total = 0
for num in arr:
    total += num 
    print(total)
#output - 100

#max element :
max_num = arr[0]
for num in arr:
    if num > max_num :
        max_num = num
print(max_num)
#output - 40

#min element :
min_num = arr[0]
for num in arr :
    if num < min_num :
        min_num = num
print(min_num)
#output - 10

#linear search :
target = 30
for i in range(len(arr)):
    if arr[i] == target :
        print("Found")
#output - Found

#count even numbers :
count = 0
for num in arr:
    if num%2 == 0:
     count += 1
print(count)
#output - 4

#odd numbers :
count = 0
for num in arr :
    if num%2 == 0:
        count = 0
    else :
        count += 1
print(count)
#output - 0

