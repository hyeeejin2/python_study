# 외장 함수


# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있음

# pickle은 객체 형태를 유지하여 파일에 저장 및 읽기가 가능
# 읽고 쓰는 파일은 무조건 binary 형식으로 해야함
import pickle
f1=open("test.txt",'wb')
data=["혜진","toin"]
pickle.dump(data,f1)

f1=open("test.txt",'rb')
data=pickle.load(f1)
print(data)
f1.close()

# os 모듈은 os 자원을 제어할 수 있음
import os
print(os.environ) # 현재 시스템의 환경 변수 값
print(os.environ['PATH'])
print(os.chdir("C:\\Users")) # 디렉터리 위치 변경
print(os.getcwd()) # 현재 디렉터리 위치
print(os.system("ipconfig")) # 시스템 명령어 호출 ""안에는 명령어
f2=os.popen("ipconfig") # 시스템 명령어의 실행 결과값을 읽기 모드 파일로 반환
print(f2.read())

# shutil은 파일을 복사해주는 모듈
import shutil
shutil.copy('C:\\Users\\vlxjf\\Documents\\Pycharm\\study\\study0719\\test.txt', "C:\\Users\\vlxjf\\Documents\\Pycharm\\study\\study0719\\test_copy.txt")

# glob 모듈은 특정 디렉터리에 존재하는 파일들을 리스트로 만들어줌
import glob
file_list=glob.glob("C:\\Users\\vlxjf\\Documents\\Pycharm\\study\\study0719\\*")
print(file_list)

# tempfile 모듈은 파일을 임시로 만들어서 사용할 때 유용함
import tempfile
filename=tempfile.mktemp() # 임의의 이름으로 파일을 만든다
print(filename)
f3=tempfile.TemporaryFile() # 임시 저장 공간으로 사용할 파일 객체를 반환, wb모드임
f3.close() # 이때 객체가 사라짐

# time 시간과 관련된 모듈
import time
print(time.time()) # UTC를 사용하여 70년 1월 1일을 기준으로 지난 시간을 초 단위로 반환
print(time.localtime(time.time())) # time.time()값을 연, 월, 일 등의 형태로 바꿈
print(time.asctime(time.localtime(time.time()))) # time.localtime(time.time())값을 보기 쉽게 바꿈
print(time.ctime()) # 위에 것을 간단하게 표시
print(time.strftime("%Y %m %d %a %I %M", time.localtime(time.time()))) # 출력 포멧으로 자세히 표시

for i in range(1,5):
   print(i)
   time.sleep(1) # 1초 간격으로 숫자 출력

# calendar 모듈을 달력을 볼 수 있음
import calendar
print(calendar.calendar(2019)) # 2019 모든 달력 출력
print(calendar.prmonth(2019,7)) # 2019년 7월 달력만 출력
print(calendar.weekday(2019,7,19)) # 요일을 숫자로 출력
print(calendar.monthrange(2019,8)) # 입력한 달의 1일이 무슨 요일인지, 그 달이 며칠까지 있는지

# random 모듈은 난수를 발생
import random
print(random.random()) # 0.0 ~ 1.0 사이의 난수 발생
print(random.randint(0,5)) # 0 ~ 5 사이의 난수 발생
def random_pop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)

if __name__=="__main__":
    data=[1,2,3,4,5]
    while data:
        print(random_pop(data))

# webbrowser 모듈은 웹 브라우저를 실행한다
import webbrowser
webbrowser.open("http://google.com")
webbrowser.open_new("http://google.com") # 새 창