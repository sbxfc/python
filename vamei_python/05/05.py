#coding=utf-8

'''
if语句
'''

i = 1
x = 1
if i > 0:
    x = x+1
print x


i = 1
if i > 0:
    print 'positive i'
    i = i + 1
elif i == 0:
    print 'i is 0'
    i = i * 10
else:
    print 'negative i'
    i = i - 1

print 'new i:',i


i  = 5
if i > 1:
    print 'i bigger than 1'
    print 'good'
    if i > 2:
        print 'i bigger than 2'
        print 'even better'
