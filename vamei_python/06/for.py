#coding=utf-8

for a in [3,4.4,'life']:
    print a


'''
range()是一个建表函数。这个表的元素都是整数，从0开始，下一个元素比前一个大1， 直到函数中所写的上限 （不包括该上限本身）
'''
idx = range(5)
print idx


for a in range(10):
    print a**2

i = 0
while i < 10:
    print i
    i = i + 1

print ('--->')

for i in range(10):
    if i == 2: 
        continue
    print i

print ('--->')

for i in range(10):
    if i == 2:        
        break
    print i
