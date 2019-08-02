# a=1
# b=3
# print(a+b)

# a=1.2
# print(a)

# a=4.24e10
# print(a)

# multiline="""Hello
# hyejin"""
# print(multiline)

# string="\"hyejin\'s\""
# print(string)

# string="hello"
# print(string*3)
# print(len(string))
# print(string[0],string[-2])

# a="Hello everyone"
# print(a[6:-3])

# a="Hello"
# string='C'+a[1:]
# print(string)

# a="Hello"
# a[0]='C'
# print(a) #error

# print("3+4=%d" %7)
# print("Hello %s" %"World")
# number=123
# a="abcdefg"
# print("%d %s" %(number,a))
# print("%d%%" %90)

# print("I eat {0} apples".format(3))
# print("I eat {0} apples".format("three"))
# number=3
# day="three"
# print("I eat {0} apples".format(number))
# print("I eat {0} apples. so I was sick for {1} days".format(number,day))
# print("I eat {number} apples. so I was sick for {day}".format(number=1,day=1))

# print("{0:*>10}".format("hi"))
# print("{0:=<10}".format("hi"))
# print("{0:-^10}".format("hi"))
# print("{0:*>10.2f}".format(3.141592))
# print("{a:10.2f}".format(a=3.141592))

# name=" hyejin "
# age=21.2525
# print(f"나의 이름은 {name}이고, 나이는 {age}입니다.")
# # print(f"{name:=^10}")
# # print(name.count('e'))
# # print(name.find('n'))
# # print("-".join(name))
# # print(name.upper())
# # print(name.lower())
# print(name.lstrip(),name.rstrip(),name.strip())
# print(name.replace("hye","jin"))

# string="Hello World"
# print(string.split(' '))

# list=[10,20,30,"a","b","c"]
# print(list[0]+list[1])
# print(list[0:3])
# print(list[-1])

# a=[1,2,3,['a','b']]
# print(a[3][-2])
# b=[1,2,[3,[4]]]
# print(b[2][1][0])
# c=[1,2,3,['a','b','c']]
# print(c[3][:2])

# a=[1,2]
# b=[3,4]
# c=["Hello"]
# d=["hyejin"]
# print(a+b)
# print(c+d)
# print(a*3)
# print(len(a),len(c))
# print(str(a[0])+"hello")
# a[1]=3
# print(a)
# del a[:]
# print(a)

# a = [1, 2, 3]
# a.append(4)
# a.append([5,6])
# print(a)
# print(a.append(4)) #append 함수 반환값이 return 이므로 None을 돌려준다 그래서 None이 출력됨

# a=[10,2,80,35,5,56]
# a.sort()
# print(a)
# b=['c','g','a','z','u']
# b.sort()
# print(b)

# a=[2,5,1,"hello"]
# a.reverse()
# print(a)
# a.reverse()
# print(a.index(5))
# a.insert(0,3)
# print(a)
# a.remove("hello")
# print(a)
# a.pop()
# print(a)
# a.extend([4,6,7,8])
# print(a)

# t1=()
# t2=(1,)
# t3=(1,2,3)
# t4=4,5,6
# t5=(1,2,(3,4))

# print(t3[:2])
# print(t3[1])
# print(t3+t4)
# print(t3*2)
# print(len(t3))

# dic={'name':'hyejin','age':'21','birthday':'0329','favorite':['food','clothes']}
# a={'1a':'a'}
# a['2b']='b'
# a['3c']=['c','c','c']
# print(a)
# del a['1a']
# print(a)
# print(dic['name'])
# b={('toin','hyejin'):'wonju','school':'daegu'}
# print(b[('toin','hyejin')])

# a={'a':1,'b':2,'c':3}
# print(a.keys())
# print(list(a.keys()))
# print(a.values())
# print(list(a.values()))
# print(list(a.items()))
# print(a.get('b'),a.get('d',4))
# print('d' in a)
# a.clear()
# print(a)

# s1=set([1,2,3])
# print(s1)
# s2=set("Hello")
# print(s2)
# l1=tuple(s1)
# print(l1,l1[0])
# l2=list(s2)
# print(l2,l2[0])

# s1=set([1,2,3,4,5,6])
# s2=set([4,5,6,7,8,9])
# print(s1&s2, s1|s2,s1-s2)
# print(s1.intersection(s2),s1.union(s2),s1.difference(s2))

# s1 = set([1, 2, 3])
# s1.add(4)
# s1.update([5, 6])
# s1.remove(1)
# print(s1)
# s2 = set("hello")
# s2.update("World")
# #s2.add("World")는 World 자체가 하나로 추가됨
# print(s2)

# a = [1, 2, 3]
# b = ["hello", "hi"]
# print(1 in a, 4 in a)
# print("hello" in b,"cello" in b)
# if 1 in a:
#     print("True")
# else:
#     print("False")

# if "hi" in b:
#     pass
# else:
#     print("False")

# if "hello" in b:print("True")
# elif "hi" in b:pass
# else:print("False")

# promot="""
#     1. Add
#     2. Del
#     3. List
#     4. Quit
#
#     Enter number: """
#
# number=0
# while number!=4:
#     print(promot)
#     number=int(input())
#
# coffee=10
# money=300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee-=1
#     print("남은 커피의 양은 %d개입니다." % coffee)
#     if coffee==0:
#         print("coffee sold out")
#         break;

# coffee=10
# while True:
#     money=int(input("돈을 넣어주세요: "))
#     if money<300:
#         print("금액이 부족합니다.")
#         break;
#     elif money>=300:
#         while True:
#             print("커피를 줍니다.")
#             money-=300
#             coffee-=1
#             if money<300:
#                 print("거스름돈 %d입니다." %money)
#                 break;

# a=0
# while a<10:
#     a+=1
#     if a%2==0:continue
#     print(a)


# marks=[50,60,80,20,90,30]
# number=0
# for mark in marks:
#     number+=1
#     if mark>=60:print("%d번 학생은 합격입니다." % number)
#     else:print("%d번 학생은 불합격입니다." % number)

# marks=[50,60,80,20,90,30]
# number=0
# for mark in marks:
#     number+=1
#     if mark>=60:print("%d번 학생은 합격입니다. 축하합니다." % number)
#     else:continue

# for i in range(1,5):
#     if i==3:
#         pass
#     print(i)
# for i in range(1,5):
#     if i==3:
#         continue
#     print(i)

# a=range(0,5)
# print(a)
# b=range(5,10)
# print(b)

# sum=0
# for i in range(1,11):
#     if i%2!=0:sum+=i
# print(sum)

# a=[1,2,3,4]
# for i in range(len(a)):
#     if a[i]<4:
#         print("4미만")
#     else:
#         print("4이다")

# for i in range(1,10):
#     for j in range(1,10):
#         print("%d * %d = %d\t" %(j,i,i*j), end='')
#     print()

# a=[1,2,3,4]
# result=[num*2 for num in a if num %2==0]
# print(result)

# result=[x*y for x in range(1,10)
#             for y in range(1,10)]
# print(list(set(result)))

# a="Life is too short, you need python"
#
# if "wife" in a:print("wife")
# elif "python" in a and "you" not in a:print("python")
# elif "shirt" not in a:print("shirt")
# elif "need" in a:print("need")
# else:print("none")

# sum=0
# num=1
# while num<=1000:
#     if num%3==0:sum+=num
#     num+=1
# print(sum)

# a='*'
# i=1
# while i<=5:
#     print(a*i)
#     i+=1

# for a in range(1,101):
#     print(a)

# sum=0
# a=[70,60,55,75,95,90,80,80,85,100]
# for i in a:
#     sum+=i
# print(sum/len(a))

# numbers=[1,2,3,4,5]
# result=[num*2 for num in numbers if num%2!=0]
# print(result)

# def add(a,b):
#     print(a,b)
#     return a+b
# result=add(b=3,a=7)
# print(result)

# def add_many(choice,*args):
#     if choice=="+":
#         result=0
#         for i in args:
#             result+=i
#         return result
#     elif choice=="*":
#         result=1
#         for i in args:
#             result*=i
#         return result
# result=add_many("*",1,2,3,4)
# print(result)

# def add_and_mul(a,b):
#     return a+b,a*b
# result=add_and_mul(2,3)
# result2,result3=add_and_mul(2,3)
# print(result,result2,result3)

# n1,n2=(input("두 수를 입력하세요 : ")).split()
# n1=int(n1)
# n2=int(n2)
# print("%d" %(n1+n2))

# f = open("test.txt", "w")
# for i in range(1,5):
#     a="""test %d
# """ %i
#     f.write(a)
# f.close()

# f=open("test.txt",'a')
# for i in range(5,10):
#     a="""test %d
# """ %i
#     f.write(a)
# f.close()

# f=open("test.txt",'r')
# while True:
#     line=f.readline()
#     if not line:break
#     print(line, end='')
# f.close()

# f=open("test.txt",'r')
# lines=f.readlines()
# for line in lines:
#     print(line,end='')
# print(lines)
# f.close()

# f=open("test.txt",'r')
# data=f.read()
# print(data)
# f.close()

# with open("test.txt","r") as f:
#     while True:
#         line=f.readline()
#         if not line:break
#         print(line, end='')

# def is_odd(number):
#     if number%2==0:print("짝수")
#     elif number%2!=0:print("홀수")
# number=int(input("자연수를 입력하세요 : "))
# is_odd(number)

# input1=int(input("첫 번째 숫자를 입력 : "))
# input2=int(input("두 번째 숫자를 입력 : "))
#
# total=input1+input2
# print("두 수의 합은 %d" %total)

# print("you" "need" "python")
# print("you"+"need"+"python")
# print("you", "need", "python") #결과 값이 다름
# print("". join(["you", "need", "python"]))

# f1=open("test.txt",'w')
# f1.write("Life is too short")
#
# f1=open("test.txt",'r')
# while True:
#     line=f1.readline()
#     if not line:break
#     print(line)
# f1.close()

# f=open("test.txt",'r')
# line=f.readline()
# if not line:
#     f=open("test.txt",'w')
#     string=input("파일이 비었습니다. 내용을 입력하세요. : ")
#     f.write(string)
# else:
#     f=open("test.txt",'a')
#     string=input("기존 내용 뒤에 입력합니다. : ")
#     f.write(string)
# f.close()

# f=open("test.txt",'r')
# string=f.read()
# string=string.replace("java","python",1)
# f=open("test.txt","w")
# f.write(string)
# f.close()

# def average(*args):
#     result=0
#     for i in args:
#         result+=i
#     return result
#
# aver_result=average(10,20,30,40,50)
# print(aver_result)

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        result=self.num1+self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def div(self):
        result = self.num1 / self.num2
        return result

class MoreCalculator(Calculator):
    def pow(self):
        result=self.num1**self.num2
        return result
    def div(self):
        if self.num2==0:return 0
        else:return self.num1/self.num2

# a=Calculator(5,2)
# b=Calculator(4,2)
# print(a.add(), a.sub(), a.mul(), a.div())
# print(b.add(), b.sub(), b.mul(), b.div())

c=MoreCalculator(3,2)
d=MoreCalculator(3,0)
print(c.div(), d.div())