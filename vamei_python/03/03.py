#coding=utf-8
s1 = (2, 1.3, 'love', 5.6, 9, 12, False)
s2 = [True, 5, 'smile']
print s1,type(s1)
print s2,type(s2)

s3 = [1,[3,4,5]]
print s3

s4 = []
print s4

print s1[0]

print s2[2]

print s3[1][2]

s2[1] = 3.0

print s2

'''
从开始到下标4 （下标5的元素 不包括在内）
'''
print s1[:5] 

'''
从下标2到最后
'''
print s1[2:]  

'''
从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）
'''
print s1[0:5:2] 

'''
从下标2到下标1
'''
print s1[2:0:-1]

'''
序列最后一个元素
'''
print s1[-1]  

'''
序列倒数第三个元素
'''
print s1[-3]  


'''
字符串是一种特殊的元素，因此可以执行元组的相关操作。
'''
str = 'abcdef'
print str[2:4]

'''
tuple元素不可变，list元素可变
序列的引用 s[2], s[1:8:2]
字符串是一种tuple
'''



