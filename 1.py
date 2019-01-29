'''
#用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
def foo(x,y):
    import os
    os.rename(x,y)
foo('/home/ht/test/a11.txt','a1')
'''
'''
#计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def tongji(str):
    num = 0
    string = 0
    space = 0
    other = 0
    for i in str:
        if i.isspace():
            space+=1
        elif i.isdigit():
            num+=1
        elif i.isalpha():
            string+=1
        else:
            other+=1
    return num,string,space,other
s = input('>:')
print(tongji(s))
'''
'''
#判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def foo(s):
    if len(s) > 5:
        print('长度大于5')
    else:
        print('长度不大于5')
s = input('>:')
foo(s)
'''
'''
#检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def f1(li):
    if len(li) >2 :
        return li[0:1]
s = input('>:')
foo(s)
'''
'''
#写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def f2(s):
    a =[]
    for i in range(len(s)):
        if i % 2 == 1:
            a.append(s[i])
    return a
print(f2([1,3,6,9,0,8]))
'''

#检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def f3(s):
    for k in s.keys():
        for v in s.values():
            if len(v) >2 :
                s[k]=v[0:1]
    return s

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
print(f3(dic))
