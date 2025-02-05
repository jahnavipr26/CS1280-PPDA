sum = 0
newlist = [] 
size = int(input('Enter size of the list: '))
for i in range(size):
  a = int(input('Enter a number: '))
  newlist.append(a)
for x in newlist:
  sum += x
print('Sum =', sum)9
print('Average =', sum / float(size))
