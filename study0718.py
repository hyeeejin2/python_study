# 내장 함수


# abs(x)는 임의의 숫자를 입력받았을 때 절댓값을 반환
print(abs(3), abs(-3))
print(abs(-5.5), abs(5.5))
print(abs(5 + 0.3))

# all(x)는 반복 가능한 자료형(리스트, 튜플, 문자열, 딕셔너리, 집합 등)을 입력 받아
# x가 모두 참이면 True, 거짓이 하나라도 있으면 False
# any(x)는 x 중에서 하나라도 참이 있으면 True, 모두 거짓이어야 False
# all <-> any
a = [1, 2, 3]
b = (0, 1, 2)
c = ''
d = {"name": "hyejin", "age": 21}
e = set([1, 0, 2])
print(all(a), all(b), all(c), all(d), all(e))
print(any(a), any(b), any(c), any(d), any(e))

# chr(i)는 아스키코드 값을 입력 받아 해당하는 문자를 출력
print(chr(65), chr(97), chr(66), chr(98))

# ord(c)는 문자의 아스키코드 값을 반환
print(ord('A'), ord('a'), ord('B'), ord('b'))

# dir은 객체가 갖고 있는 변수나 함수를 보여줌
li_ = [1, 2, 3]
dic = {1: a, 2: b, 3: c}
print(dir(li_))
print(dir(dic))

# divmod(a, b)는 2개의 숫자를 입력받고 a/b의 몫과 나머지를 반환
print(divmod(25, 5), divmod(20, 3))

# enumerate는 순서가 있는 자료형을 입력 받아 현재 인덱스 값과 그 값을 알려준다
li = [123, 456, 789]
for i, value in enumerate(li):
    print(i + 1, ':', value)

# eval은 실행 가능한 문자열을 입력 받아 실행값을 돌려줌
print(eval('1+2'), eval('4/2'), eval("'hello '+'world'"), eval('chr(97)'), eval('divmod(5,2)'))

# filter는 반환 값이 참인 것만 묶어서 필터링함
def positive(x):
    return x > 0

print(list(filter(positive, ([1, -3, 2, 0, -5, 6]))))
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# map(f, iterable)은 함수와 반복 가능한 자료형을 입력 받아 함수가 수행한 결과를 반환
def two_times(x):
    return x * 2

print(list(map(two_times, [1, 2, 3, 4])))
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))

# hex는 정수 값을 입력 받아 16진수 값으로 변환
print(hex(10), hex(11))

# int(x)는 정수 형태로 반환함
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환
print(int(5.5), int(6.22))
print(int('100', 16))  # 해석 : 16진수 100을 10진수로 바꿔준다

# oct(x)는 정수를 8진수 문자열로 바꿔서 반환
print(oct(10), oct(100))

# id는 입력받은 객체의 주소 값을 돌려줌
f = 1
g = f
print(id(f), id(1), id(g))

# input() 사용자 입력 함수, 입력 받은 것은 문자열로 인식
# string=input("문자열을 입력 : ")
# number=int(input("정수를 입력 : "))
# print(string, number)

# isinstance(object, class)는 입력받은 인스터스가 그 클래스의 인스턴스인지 판단
# 참이면 True, 거짓이면 False
class A:
    pass

a2 = A()
a3 = 3
print(isinstance(a2, A), isinstance(a3, A))

# len(s)은 s의 길이를 반환
h = [1, 2, 3, 4, 5, 6]
print(len(h))

# list(s)는 반복 가능한 자료형을 입력 받아 리스트로 만들어 반환
print(list("hello"), list((1, 2, 3)))

# str(object)는 객체를 문자열 형태로 변환하여 반환
k = str('123')
l = str('HELLO')
m = str('HELLO'.lower())
print(k, l, m)
print(str('123'), str('HELLO'), str('HELLO'.lower()))

# tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꿔서 반환
print(tuple("123"), tuple([1, 2, 3]))

# max(iterable)은 반복 가능한 자료형을 입력 받아 최댓값을 반환
# min(iterable)은 반복 가능한 자료형을 입력 받아 최솟값을 반환
print(max(10, 2, 50, 22), min(10, 2, 50, 22))

# open(filename, mode) filename 파일을 mode로 열기
fp = open("test.txt", 'r')
fp.close()

# pow(x,y)는 x의 y제곱한 결과를 반환 **연산자와 같다
print(pow(4, 2), 4 ** 2)

# range(start,stop)는 start부터 stop-1까지 값은 반복 가능한 객체로 만들어줌
print(list(range(3)), list(range(1, 5)), list(range(1, 10, 2)))  # 인수가 3개인 경우의 마지막 숫자는 사이 거리

# round(number[, ndigits])는 입력 받은 숫자를 반올림 함
print(round(4.3), round(4.6), round(5.2), round(6.286, 1), round(5.812, 2))  # 인수가 2개인 경우의 마지막 숫자는 소수점 n자리까지 반올림하여 표시함

# sorted(iterale)는 입력값을 정렬 후 리스트로 반환, 리스트 자료형의 sort함수는 리스트 객체 자체를 정렬만 함
i = sorted([2, 5, 0, 1, 3, 4])
j = [2, 5, 0, 1, 3, 4]
j.sort()
print(i, j)

# sum(iterable)은 입력받은 리스트 or 튜플의 모든 요소의 합을 돌려주는 함수
print(sum([1, 3, 5, 7, 9]), sum((2, 4, 6, 8, 10)))

# type(object)은 입력값의 자료형을 알려줌
print(type("hyeijn"), type(10), type([1, 2, 3]), type((1, 2, 3)), type({1: 'a', 2: 'b'}))

# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어줌
string_ = "HYEJIN"
list_ = [1, 2, 3, 4, 5, 6]
tuple_ = ('w', 'o', 'n', 'j', 'u', '*')
dic_ = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}

print(list(zip(string_, list_,tuple_)))
print(list(zip(string_,dic_))) # 딕셔너리는 key, value 값으로만 구성되어 있으므로 2개까지만 묶을 수 있음