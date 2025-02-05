list1, list2 = [], [] 
size = int(input('Enter size of the list: '))
for i in range(size):
  num = int(input('Enter a number: '))
list1.append(num)
print('The input list is:')
print(list1)
for i in list1:
  if 1 <= i <= 100:
    list2.append(i)
print('The new list is:')
print(list2)
