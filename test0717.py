# # 모듈 실습
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# if __name__=="__main__":
#     print(add(5,3), sub(5,3))
#
# PI=3.141592
#
# class Math:
#     def solv(self,r):
#         return PI*(r**2)
#
# def add(a,b):
#     return a+b

# 예외 처리

# try:
#     a=[1,2,3]
#     print(a[4])
#     print(4/0)
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 범위를 벗어났습니다.")

# try:
#     a=[1,2,3]
#     print(a[4])
#     print(4/0)
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# try:
#    a=[1,2,3]
#    print(4 / 0)
#    print(a[4])
# except (ZeroDivisionError, IndexError) as e:
#    print(e)

# try:
#    a=[1,2,3]
#    print(4 / 0)
#    print(a[4])
# except (ZeroDivisionError, IndexError) as e:
#    pass

# class hyejin:
#    def people(self):
#        raise NotImplementedError

# class toin:
#    def people(self):
#         print("I'm toin")

# person=toin()
# person.people()

# class Error(Exception):
#    pass

# def say(s):
#    if s=="참새":
#        raise Error()
#    print(s)
    
# say("혜진")
# say("참새")

# class Error(Exception):
#    def __str__(self):
#        return "잘못되었습니다. 오류입니다"
#    pass

# def say(s):
#    if s=="써트장":
#        raise Error()
#    print(s)

# try:
#    say("혜진")
#    say("토인")
#    say("참새")
#    say("써트장")
# except Error as e:
#    print(e)
