import os

os.remove("X:/fuck.txt")
wife=['nana7mi']
print('我的老婆是'+wife[0])
pigwife='你老婆是大飞柱？真恶心'
singledog='哦你没有老婆，哈哈单身狗'
sb=open("X:/fuck.txt","a+")
yes_or_no=input('你有老婆吗？yes or no')
if yes_or_no=='yes':
       whowife=input('你老婆是谁呀？')
       if whowife == '33':
            print(pigwife,file=sb)
       elif whowife == 'T33':
            print(pigwife,file=sb)
       elif whowife == '谭杉杉':
            print(pigwife,file=sb)
       else:
            wife.append(whowife)
            print('我老婆有:',file=sb)
            print(wife,file=sb)
            print('Now',whowife,'is my wife',file=sb)
elif yes_or_no=='no':
    print(singledog,file=sb)
else:
    print('看不懂文字吗？yes or no啊',file=sb)