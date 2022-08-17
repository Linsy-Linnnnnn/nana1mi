m=1
n=2
print('sb:\n"cnm"')#转义字符反斜线\，赋予字母不同含义
print(m,"m")

sb=open("X:/fuck.txt","a+")
print("Cnm\nnmsl",m,n,(m+n),file=sb)

print(ord("臭"),ord("鲨"),ord("鱼"),ord("我"),ord("爱"),ord("你"))#ord表示转换为十进制字符代码

print(chr(33261)+chr(40104)+chr(40060)+chr(25105)+chr(29233)+chr(20320))#chr表示将十进制代码转化为字符（二进制需要在前面加0b）（0bxxxxx)

cpdd=114514
cpdd=1919810
print(cpdd)#对一个命名赋予数据，如果给这个命名一个新的数据，则会顶替掉上一个数据

name = "aza sex with 本帅"
print(name.title())#每个单词第一个字母变大写
print(name.upper())#所有字母变大写
print(name.lower())#所有字母变小写
